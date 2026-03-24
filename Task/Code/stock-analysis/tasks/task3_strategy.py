import pandas as pd
import os

# base directory path for data 
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "..", "data", "stock1.csv")

# this function will help to find time based strategy
def run_strategy(df):
    df['Date'] = pd.to_datetime(df['Date'])
    df['Day'] = df['Date'].dt.day_name()

# trades logs buying and selling
    trades = []

    buy_price = None

#loop through the dataframe and csv files
    for i in range(len(df)):
        row = df.iloc[i]

# if day is monday then only buy the stock
        if row['Day'] == 'Monday':
            buy_price = row['Close']

# if day is friday then only sell the stock and if not buy then skip
        elif row['Day'] == 'Friday' and buy_price is not None:
            sell_price = row['Close']

            #calculating profit
            profit = sell_price - buy_price

            trades.append({
                "Buy": float(buy_price),
                "Sell": float(sell_price),
                "Profit": float(profit)
            })

            buy_price = None

    return trades


# main funtion
def main():
    df = pd.read_csv(file_path)

    trades = run_strategy(df)

    #calculating total profit tilll now 
    total_profit = sum(t['Profit'] for t in trades)

    print("\n Trade Logs for monday buy and friday selles :")
    for t in trades:
        print(t)

    print(f"\n Final performance of all trades : {total_profit:.2f}")


if __name__ == "__main__":
    main()