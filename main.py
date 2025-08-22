
import math
import scipy as sp
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def main():
    print("Black-Scholes Model")

    # Define parameters
    S = 100         
    K = 100         
    T = 1           
    r = 0.05       
    sigma = 0.2

    call_option = calc_call_option(S, K, T, r, sigma)
    put_option = calc_put_option(S, K, T, r, sigma)

    print(f"Call Option Price: {call_option}")
    print(f"Put Option Price: {put_option}")

def calc_call_option(S, K, T, r, sigma):
    d1 = calc_d1(S, K, T, r, sigma)
    d2 = calc_d2(d1, sigma, T)
    call_price = (S * sp.stats.norm.cdf(d1) - K * math.exp(-r * T) * sp.stats.norm.cdf(d2))
    return call_price

def calc_put_option(S, K, T, r, sigma):
    d1 = calc_d1(S, K, T, r, sigma)
    d2 = calc_d2(d1, sigma, T)
    put_price = (K * math.exp(-r * T) * sp.stats.norm.cdf(-d2) - S * sp.stats.norm.cdf(-d1))
    return put_price

def calc_d1(S, K, T, r, sigma):
    d1 = (math.log(S / K) + (r + 0.5 * (sigma * sigma)) * T) / (sigma / math.sqrt(T))
    return d1

def calc_d2(d1, sigma, T):
    d2 = d1 - sigma * math.sqrt(T)
    return d2

if __name__ == "__main__":
    main()


