import pandas as pd

def calculate_moving_average(df, window):
    df['MA'] = df['Close'].rolling(window=window).mean()
    return df

def is_price_above_ma(df):
    return df['Close'].iloc[-1] > df['MA'].iloc[-1]

def is_volume_increasing(df, lookback=5):
    recent_volume = df['Volume'].tail(lookback)
    return recent_volume.is_monotonic_increasing