Black-Scholes Formula Calculator

Author: Arjun Vivek Kumar

Description: This project implements the Black-Scholes formula for pricing European call and put options. The model calculates fair option prices baed on stock price, strike price, volatility, risk-free interest rate, and time to expiration. 

Assumptions: 
- Stock prices follow a geometric Brownian Motion
- Returns (log-returns) are normally distributed
- Stock prices are log-normal
- No transaction costs, taxes
- Buy and sell as much as you want at the current price
- Risk-free interest rate r is constant and known in advance
- Option is European style (can only be exercised at maturity, not before)
- Strike price K and maturity T is known and fixed
- Frictionless and arbitrage-free markets
- No dividend pay 

Formula:
C = S​ * N(d1​) − K * (e^−rT) * N(d2​)
P = K * (e^−rT) * N(-d2​) - S * N(-d1)

d1 = (ln(S/K) + (r + 1/2 * σ^2)T) / σ/√T
d2 = d1 - σ/√T

S = Current stock price
K = Strike price
T = Time to expiration
r = Risk-free interest rate
σ = Volatility
N() = Standard normal cumulative distribution function (CDF)

Greek Implementation:

Delta   -> Sensitivity to stock price
Gamma   -> Sensitivity of Delta to stock price
Vega    -> Sensitivity to volatility
Theta   -> Sensitivity to time
Rho     -> Sensitivity to interest rate