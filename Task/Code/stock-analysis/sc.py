import pandas as pd
import numpy as np
import config

risk_rate = 0.01

def calculate_sharpe_ratio(returns, risk_free_rate=risk_rate):
    excess_returns = returns - risk_free_rate/252
    return np.mean(excess_returns) / np.std(excess_returns)


def calculate_volatility(returns):
    return np.std(returns) * np.sqrt(252)


def calculate_max_drawdown(returns):
    cumulative = (1 + returns).cumprod()
    peak = cumulative.cummax()
    drawdown = (cumulative - peak) / peak
    return drawdown.min()


def main():
    df = pd.read_csv("data/returns.csv")

    returns = df['Returns']

    sharpe = calculate_sharpe_ratio(returns)
    volatility = calculate_volatility(returns)
    max_dd = calculate_max_drawdown(returns)

    print("\n Risk Metrics Calculation based on following :")
    print(f"Sharpe Ratio  : {sharpe:.4f}")
    print(f"Volatility : {volatility:.4f}")
    print(f"Max Drawdown : {max_dd:.4f}")


if __name__ == "__main__":
    main()
