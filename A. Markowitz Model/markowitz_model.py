import numpy as np
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import scipy.optimize as optimization


NUM_OF_TRADING_DAYS = 252
NUM_PORTFOLIOS = 10000

class MarkowitzModel:

    def __init__(self, stocks, start_date, end_date):
        self.stocks = stocks
        self.start_date = start_date
        self.end_date = end_date

    def download_data(self):

        stock_data = {}

        for stock in self.stocks:
            ticker = yf.Ticker(stock)
            stock_data[stock] = ticker.history(start=self.start_date, end=self.end_date)['Close']

        return pd.DataFrame(stock_data)

    def show_data(self, data):
        data.plot(figsize=(10, 5))
        plt.show()

    def calculate_return(self, data):
        # S(t) / S(t-1) 
        # Theoritically S(t + 1) / S(t)
        # Why Log return due to normalization
        log_return = np.log(data / data.shift(1)) 
        # print(log_return)
        return log_return[1:]
    
    def show_statistics(self, returns, num_of_trading_days=252):
    # Means of the Annual Returns
        means = returns.mean() * num_of_trading_days
        cov = returns.cov() * num_of_trading_days
        return means, cov
    
    def show_portfolios(self, returns, volatilities):
        plt.figure(figsize=(10, 6))
        plt.scatter(volatilities, returns, c=returns/volatilities, marker="o")
        plt.grid(True)
        plt.xlabel("Expected Volatility")
        plt.ylabel("Expected Returns")
        plt.colorbar(label="Sharpe Ratio")
        plt.show()

    def generate_portfolios(self, returns, num_portfolios=10000, num_of_trading_days=252):

        portfolio_means, portfolio_risks, portfolio_weights = [], [], []

        for _ in range(num_portfolios):
            w = np.random.random(len(self.stocks))
            # Sum of w should be 1 (100%)
            w /= np.sum(w)
            portfolio_weights.append(w)
            portfolio_means.append(np.sum(returns.mean() * w) * num_of_trading_days)
            portfolio_risks.append(
                np.sqrt(np.dot(w.T, np.dot(returns.cov() * num_of_trading_days, w)))
            )
        return np.array(portfolio_weights), np.array(portfolio_means), np.array(portfolio_risks)
    
    def statistics(self, weights, returns, num_of_trading_days=252):
        portfolio_returns = np.sum(returns.mean() * weights) * num_of_trading_days
        portfolio_volatility = np.sqrt(np.dot(weights.T, np.dot(returns.cov() * num_of_trading_days, weights)))
        sharpe_ratio = portfolio_returns / portfolio_volatility
        return np.array([portfolio_returns, portfolio_volatility, sharpe_ratio])
    
    def min_function_sharpe(self, weights, returns):
        return -self.statistics(weights, returns)[2]
    
    def optimize_portfolio(self, weights, returns):
        # the sum of weights is 1
        constraints = {"type": "eq", "fun": lambda x: np.sum(x) -1}
        # the weights can be 1 at most: 1 when 100% of money is invested into a single stock
        bounds = tuple((0, 1) for _ in range(len(self.stocks)))
        return optimization.minimize(
            fun=self.min_function_sharpe, x0=weights[0], 
            args=returns, method="SLSQP", 
            bounds=bounds, constraints=constraints
        )
    
    def print_optimal_portfolio(self, optimum, returns):
        print(f"Optimal Portfolio: {optimum['x'].round(3)}")
        print(f"Expected Return, volatility and sharpe ratio: {self.statistics(optimum['x'].round(3), returns)}")

    def show_optimal_portfolio(self, opt, rets, portfolio_rets, portfolio_vols):
        plt.figure(figsize=(10, 6))
        plt.scatter(
            portfolio_vols,
            portfolio_rets,
            c=portfolio_rets/portfolio_vols,
            marker="o"
        )
        plt.grid(True)
        plt.xlabel("Expected Volatility")
        plt.ylabel("Expected Returns")
        plt.colorbar(label="Sharpe Ratio")
        plt.plot(
            self.statistics(opt['x'], rets)[1],
            self.statistics(opt['x'], rets)[0],
            "g*"
        )
        plt.show()


stocks = ["ADANIENT.NS", "BAJAJFINSV.NS", "HPL.NS", "JINDALSTEL.NS"]
start_date = "2024-10-01"
end_date = "2025-10-03"
mm = MarkowitzModel(stocks, start_date, end_date)
stocks_df = mm.download_data()
returns_df = mm.calculate_return(stocks_df)

