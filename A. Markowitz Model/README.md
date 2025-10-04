# Markowitz Model (Modern Portfolio)

- It was first formulated by Harry Markowitz in 1952.
- He was later awarded with the Nobel Prize in Economics.
- It is a portfolio optimization model.

**Portfolio**: A portfolio is a collection of financical investments such as stocks, bonds, commodities and cash.

- Markowitz Model assists in the selection of the most efficient portfolio by considering various possible portfolios of the given securities based on Expected Return (Mean) and Risk (Variance)

## Main Idea behind Markowitz Model

- if we want to invest all of our money into a single stock then we take a huge risk because stocks are volatile
- **A single stock is quite risky - because it is unpredictable we do not know for certain whether the S(t) stock price will rise or fall.**
- we may combine multiple assets(stocks) in order to reduce risk as much as possible.
- The main conclusion of Markowitz Model is DIVERSIFICATION.

## Assumptions of Markowitz Model

1. **Returns are Normally Distributed:**: The returns of the stocks are normally distributed with $\mu$ Mean and $\sigma$ standard deviation
2. **Investors are risk averse**: Investors will take on more risk if they are expecting more return.

- If there is a low risk (bonds) the return is low as well.
- with higher risk (stocks) the returns are usually higher.
- Modern Portfolios offering the maximum possible expected return for a given level of risk.

**SO THE EFFICIENT PORTFOLIO IS THE PORTFOLIO THAT HAS THE HIGHEST REWARD FOR A GIVEN LEVEL OF RISK OR THE LOWEST RISK FOR A GIVEN RETURN**

- The investors are not allowed to setup short positions in a security so 100% of the wealth has to be divided among available assets (stocks) in a way that all positions are long positions.

Wi -> this is the weight for the ith asset or stock
ri -> this is the return for the ith asset or stock (historical data).
$\mu$ i -> this is the expected return for the ith asset or stock (Mean of the stock).

$$
ri = 
\frac{S(t+1) - S(t)}{S(t)}
$$

{this is how we can calculate the daily return of a stock.}

we have to consider neighboring [t, t+1] time steps

Usually Log of the returns is used 


$$
\ln\!\left(\frac{S(t+1)}{S(t)}\right)
$$

