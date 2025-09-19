import gradio as gr
# app = gr.Interface(
#     fn=run_dashboard,
#     inputs=[
#         gr.Dropdown(techniques, value=techniques[0], label="Select Trading Strategy"),
#         gr.Number(value=1000, label="Initial Investment"),
#         gr.Textbox(value="AAPL", label="Enter Stock Ticker"),
#         gr.Textbox(value="2024-01-01", label="Start Date (YYYY-MM-DD)"),
#         gr.Textbox(value="2025-09-17", label="End Date (YYYY-MM-DD)"),
#         gr.Number(value=20, label="Fast EMA Period"),
#         gr.Number(value=100, label="Slow EMA Period"),
#     ],
#     outputs=[
#         gr.Plot(label="Moving Average Crossover"),
#         gr.Textbox(label="Strategy Profit"),
#         gr.Plot(label="Equity Curve"),
#     ],
#     title="Trading Strategy Dashboard",
#     description="EMA Crossover Trading Strategy using Yahoo Finance data."
# )


# app.launch()