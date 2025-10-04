import streamlit as st

from moving_average_crossover import MovingAverageCrossover
from moving_avgs_with_rsi import MovingAverageRSIStrategy

# st.set_page_config(layout="wide")
# left_column, mid_column, right_column = st.columns([1, 4, 1]) # Adjust ratios as needed

# with mid_column:
#     st.header("Main Content Area")
#     st.write("This is the main content of your application.")
#     st.slider("Adjust a setting in the main area", 0, 100, 50)

# with right_column:
#     st.header("Right Panel")
#     st.write("This section acts as a right-side panel.")
#     st.button("Click me in the right panel")
#     st.text_input("Enter text in the right panel")

# with left_column:
#     st.write("Left panel")

st.title("Trading Strategies")


technique = None
button_clicked = False
with st.sidebar:

    technique = st.selectbox(
        label="Select your Trading Strategy",
        options=['Moving Average Crossover', "Moving Average with RSI"],
        index=0
    )


    stock_name = st.text_input(label="Enter Stock Name")
    initial_investment = st.number_input(label="Enter your Initial Investment", min_value=1)
    start_date = st.date_input(label="Enter Start Date")
    end_date = st.date_input(label="Enter End Date")
    short_period = st.number_input(label="Enter your Fast EMA period", min_value=10, max_value=365, step=5)
    long_period = st.number_input(label="Enter your Slow EMA period", min_value=10, max_value=365, step=5)

    button_clicked = st.button("Start")
if button_clicked:
    if technique == "Moving Average Crossover":
        strategy = MovingAverageCrossover(initial_investment, stock_name, start_date, end_date, short_period, long_period)
        with st.spinner("Downloading Stock Data"):
            strategy.download_data()
        
        strategy.construct_signals()
        st.pyplot(strategy.plot_signals())
        strategy.simulate()
        st.write(f"{strategy.strategy_profit():.2f}%")
        st.pyplot(strategy.plot_equity())
    elif technique == "Moving Average with RSI":
        strategy = MovingAverageRSIStrategy(initial_investment, stock_name, start_date, end_date, short_period, long_period)
        with st.spinner("Downloading Stock Data"):
            strategy.download_data()
        
        strategy.construct_signals()
        st.pyplot(strategy.plot_signals())
        strategy.simulate()
        st.write(f"{strategy.strategy_profit():.2f}%")
        st.pyplot(strategy.plot_equity())