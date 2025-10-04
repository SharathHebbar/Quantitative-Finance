import datetime
import gradio as gr
from yahooquery import search


def get_stock_ticker(stock_name):

    result = search(stock_name)
    return result['quotes'][0]['symbol']


def run_dashboard(technique, investment, ticker, start_date, end_date, short_period, long_period):
    if technique == "Moving Average Crossover":
        strategy = MovingAverageCrossover(investment, ticker, start_date, end_date, short_period, long_period)
        strategy.download_data()
        strategy.construct_signals()
        strategy.simulate()

        profit = f"{strategy.strategy_profit():.2f}%"
        return profit, strategy.plot_signals(), strategy.plot_equity()
    elif technique == "Moving Average with RSI":
        strategy = MovingAverageRSIStrategy(investment, ticker, start_date, end_date, short_period, long_period)
        strategy.download_data()
        strategy.construct_signals()
        strategy.simulate()

        profit = f"{strategy.strategy_profit():.2f}%"
        return profit, strategy.plot_signals(), strategy.plot_equity()


techniques = ['Moving Average Crossover', "Moving Average with RSI"]


with gr.Blocks(theme=gr.themes.Soft()) as demo:
    gr.Markdown("# Trading Strategy Dashboard")
    gr.Markdown("EMA Crossover Trading Strategy using Yahoo Finance data.")
    with gr.Row():
        with gr.Column(scale=1):

                trading_strategy = gr.Dropdown(techniques, value=techniques[0], label="Select Trading Strategy")
                investment = gr.Number(value=1000, label="Initial Investment")
                ticker = gr.Textbox(value="AAPL", label="Enter Stock Ticker")
                start_date = gr.Textbox(value="2024-01-01", label="Start Date (YYYY-MM-DD)")
                end_date = gr.Textbox(value="2025-09-17", label="End Date (YYYY-MM-DD)")
                # start_date = gr.Date(value=datetime.date(2024, 1, 1), label="Start Date")
                # end_date = gr.Date(value=datetime.date(2025, 9, 17), label="End Date")
                fast_ema = gr.Number(value=20, label="Fast EMA Period")
                slow_ema = gr.Number(value=100, label="Slow EMA Period")
                submit = gr.Button("Submit")
            # with gr.Row(scale=1):
                gr.Markdown("# Check your Stock name here.")
                stock_name = gr.Textbox(value="Apple", label="Enter Stock Name to get the ticker")
                stock_ticker = gr.Button("Get Ticker")
                ticker_name = gr.Textbox(label="Ticker Name", interactive=False, show_copy_button=True)
            
        with gr.Column(scale=3):
            with gr.Row():
                profit = gr.Textbox(label="Strategy Profit", interactive=False)
            with gr.Row():
                ma_plot = gr.Plot(label="Moving Average Crossover")
            with gr.Row():
                equity_curve = gr.Plot(label="Equity Curve")
    submit.click(
        run_dashboard,
        inputs=[trading_strategy, investment, ticker, start_date, end_date, fast_ema, slow_ema],
        outputs=[profit, ma_plot, equity_curve],
    )

    stock_ticker.click(
        get_stock_ticker,
        inputs=[stock_name],
        outputs=[ticker_name]
    )
demo.launch()
