Black-Scholes Formula Calculator

Author: Arjun Vivek Kumar

Description: This project implements the Black-Scholes formula for pricing European call and put options. The model calculates fair option prices baed on stock price, strike price, volatility, risk-free interest rate, and time to expiration. 

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