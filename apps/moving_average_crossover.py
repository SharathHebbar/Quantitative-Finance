import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import yfinance as yf
import streamlit as st

class MovingAverageCrossover:

    def __init__(self, capital, stock, start, end, short_period, long_period):
        self.data = None
        self.is_long = False
        self.short_period = short_period
        self.long_period = long_period
        self.capital = capital
        self.equity = [capital]
        self.stock = stock
        self.start = start
        self.end = end

    def download_data(self):
        ticker = yf.download(self.stock, self.start, self.end)
        stock_data = pd.DataFrame(ticker['Close'][self.stock])
        stock_data.columns = ['Price']
        self.data = stock_data

    def construct_signals(self):
        self.data['short_ema'] = self.data['Price'].ewm(span=self.short_period).mean()
        self.data['long_ema'] = self.data['Price'].ewm(span=self.long_period).mean()

    def simulate(self):
        # We consider all the trading days and decide whether to open a long position or not
        price_when_to_buy = 0
        for index, row in self.data.iterrows():
            # Closing the Long Position
            if row.short_ema < row.long_ema and price_when_to_buy > 0 and self.is_long: 
                self.equity.append((self.capital * row.Price / price_when_to_buy).item())
                self.is_long = False
                # print("SELL")
            elif row.short_ema > row.long_ema and not self.is_long:
                # Open a Long position
                price_when_to_buy = row['Price']
                self.is_long = True
                # print("BUY")
    
    def strategy_profit(self):
        profit_pct = ((float(self.equity[-1]) - float(self.equity[0])) / float(self.equity[0])) * 100
        return profit_pct

    def plot_equity(self):
        fig = go.Figure()

        fig.add_trace(go.Scatter(
            y=self.equity,
            mode="lines",
            name="Equity",
            line=dict(color="green")
        ))

        fig.update_layout(
            title="Equity Curve",
            xaxis_title="Date",
            yaxis_title="Capital ($)",
            template="plotly_white",
            width=900,
            height=500
        )

        return fig
        # # Build matplotlib figure
        # fig, ax = plt.subplots(figsize=(12, 6))
        # ax.set_title("Equity Curve")
        # ax.plot(self.equity, label="Equity", color="green")
        # ax.set_xlabel("Date")
        # ax.set_ylabel("Capital ($)")
        # ax.legend()
        # return fig

    def plot_signals(self):
        fig = go.Figure()

        fig.add_trace(go.Scatter(
            y=self.equity,
            mode="lines",
            name="Equity",
            line=dict(color="green")
        ))

        fig.update_layout(
            title="Equity Curve",
            xaxis_title="Date",
            yaxis_title="Capital ($)",
            template="plotly_white",
            width=900,
            height=500
        )

        return fig

    def plot_signals(self):
        fig = go.Figure()

        # Stock Price
        fig.add_trace(go.Scatter(
            x=self.data.index, y=self.data["Price"],
            mode="lines",
            name="Stock Price",
            line=dict(color="black")
        ))

        # Short EMA
        fig.add_trace(go.Scatter(
            x=self.data.index, y=self.data["short_ema"],
            mode="lines",
            name=f"{self.short_period} EMA",
            line=dict(color="red")
        ))

        # Long EMA
        fig.add_trace(go.Scatter(
            x=self.data.index, y=self.data["long_ema"],
            mode="lines",
            name=f"{self.long_period} EMA",
            line=dict(color="blue")
        ))

                # Layout
        fig.update_layout(
            title="Moving Average (MA) Crossover Trading Strategy",
            xaxis_title="Date",
            yaxis_title="Stock Price",
            template="plotly_white",
            width=900,
            height=500,
            legend=dict(x=0, y=1, bgcolor="rgba(0,0,0,0)")
        )
        return fig

        # fig, ax = plt.subplots(figsize=(12, 6))
        # ax.plot(self.data['Price'], label="Stock Price", color="black")
        # ax.plot(self.data['short_ema'], label=f"{self.short_period} EMA", color="red")
        # ax.plot(self.data['long_ema'], label=f"{self.long_period} EMA", color="blue")

        # ax.set_title("Moving Average (MA) Crossover Trading Strategy")
        # ax.set_xlabel("Date")
        # ax.set_ylabel("Stock Price")
        # ax.legend()
        # return fig
