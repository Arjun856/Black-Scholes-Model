from flask import Flask, request, render_template
import math
import scipy as sp

app = Flask(__name__)

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
    d1 = (math.log(S / K) + (r + 0.5 * (sigma * sigma)) * T) / (sigma * math.sqrt(T))
    return d1

def calc_d2(d1, sigma, T):
    d2 = d1 - sigma * math.sqrt(T)
    return d2

def calc_call_delta(S, K, T, r, sigma):
    d1 = calc_d1(S, K, T, r, sigma)
    call_delta = sp.stats.norm.cdf(d1)
    return call_delta

def calc_put_delta(S, K, T, r, sigma):
    d1 = calc_d1(S, K, T, r, sigma)
    put_delta = sp.stats.norm.cdf(d1) - 1
    return put_delta

def calc_gamma(S, K, T, r, sigma):
    d1 = calc_d1(S, K, T, r, sigma)
    gamma = sp.stats.norm.pdf(d1) / (S * sigma * math.sqrt(T))
    return gamma

def calc_vega(S, K, T, r, sigma):
    d1 = calc_d1(S, K, T, r, sigma)
    vega = S * sp.stats.norm.pdf(d1) * math.sqrt(T)
    return vega

def calc_call_theta(S, K, T, r, sigma):
    d1 = calc_d1(S, K, T, r, sigma)
    d2 = calc_d2(d1, sigma, T)
    call_theta = (-S * sp.stats.norm.pdf(d1) * sigma / (2 * math.sqrt(T)) -
                  r * K * math.exp(-r * T) * sp.stats.norm.cdf(d2))
    return call_theta

def calc_put_theta(S, K, T, r, sigma):
    d1 = calc_d1(S, K, T, r, sigma)
    d2 = calc_d2(d1, sigma, T)
    put_theta = (-S * sp.stats.norm.pdf(d1) * sigma / (2 * math.sqrt(T)) +
                  r * K * math.exp(-r * T) * sp.stats.norm.cdf(-d2))
    return put_theta

def calc_call_rho(S, K, T, r, sigma):
    d1 = calc_d1(S, K, T, r, sigma)
    d2 = calc_d2(d1, sigma, T)
    call_rho = K * T * math.exp(-r * T) * sp.stats.norm.cdf(d2)
    return call_rho

def calc_put_rho(S, K, T, r, sigma):
    d1 = calc_d1(S, K, T, r, sigma)
    d2 = calc_d2(d1, sigma, T)
    put_rho = -K * T * math.exp(-r * T) * sp.stats.norm.cdf(-d2)
    return put_rho

@app.route("/", methods=["GET", "POST"])
def main(): 
    # Initialize Values
    S = 100
    K = 100
    T = 1
    r = 5
    sigma = 20
    call_price = None
    put_price = None
    
    # Initialize Greeks
    call_delta = None
    put_delta = None
    gamma = None
    vega = None
    call_theta = None
    put_theta = None
    call_rho = None
    put_rho = None
    error = None

    if request.method == "POST":
        try:
            S = float(request.form.get("S", 100))
            K = float(request.form.get("K", 100))
            T = float(request.form.get("T", 1))
            r = float(request.form.get("r", 5)) / 100  
            sigma = float(request.form.get("sigma", 20)) / 100  

            # Calculate prices
            call_price = calc_call_option(S, K, T, r, sigma)
            put_price = calc_put_option(S, K, T, r, sigma)
            
            # Calculate Greeks
            call_delta = calc_call_delta(S, K, T, r, sigma)
            put_delta = calc_put_delta(S, K, T, r, sigma)
            gamma = calc_gamma(S, K, T, r, sigma)
            vega = calc_vega(S, K, T, r, sigma)
            call_theta = calc_call_theta(S, K, T, r, sigma)
            put_theta = calc_put_theta(S, K, T, r, sigma)
            call_rho = calc_call_rho(S, K, T, r, sigma)
            put_rho = calc_put_rho(S, K, T, r, sigma)
            
        except Exception as e:
            error = f"Calculation error: {str(e)}"
    
    # Always pass all values back to template
    return render_template("index.html", 
                          call_price=call_price, 
                          put_price=put_price,
                          call_delta=call_delta,
                          put_delta=put_delta,
                          gamma=gamma,
                          vega=vega,
                          call_theta=call_theta,
                          put_theta=put_theta,
                          call_rho=call_rho,
                          put_rho=put_rho,
                          S=S, 
                          K=K, 
                          T=T, 
                          r=r*100 if isinstance(r, float) else r,  
                          sigma=sigma*100 if isinstance(sigma, float) else sigma,
                          error=error)

if __name__ == "__main__":
    app.run(debug=True)

