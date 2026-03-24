import os
import sys

import pandas as pd
from utils.indicators import (
    calculate_moving_average,
    is_price_above_ma,
    is_volume_increasing
)
import config


def process_stock(file_path):
    try:
        df = pd.read_csv(file_path)

        # Ensure required columns exist
        required_cols = ['Close', 'Volume']
        if not all(col in df.columns for col in required_cols):
            print(f"Skipping {file_path}: Missing columns")
            return None

        if 'Date' in df.columns:
            df = df.sort_values(by='Date')

        # Check minimum data for all .csv file contain or not
        if len(df) < config.MOVING_AVG_WINDOW:
            print(f"Skipping {file_path}: Not enough data")
            return None

        # Calculate indicators
        df = calculate_moving_average(df, config.MOVING_AVG_WINDOW)

        # check all conditions thats satisfy or not
        price_cond = is_price_above_ma(df)
        volume_cond = is_volume_increasing(df, config.VOLUME_LOOKBACK)

        if price_cond and volume_cond:
            return os.path.basename(file_path)

    except Exception as e:
        print(f"Error processing {file_path}: {e}")

    return None


def main():
    selected_stocks = []

    for file in os.listdir(config.DATA_FOLDER):
        file_path = os.path.join(config.DATA_FOLDER, file)

        if file.endswith(".csv"):
            result = process_stock(file_path)
            if result:
                selected_stocks.append(result)

    # Output results and print in terminl
    print("\n Selected Stocks:")
    for stock in selected_stocks:
        print(stock)

    # Save to CSV file in output/result.csv
    if selected_stocks:
        df_out = pd.DataFrame(selected_stocks, columns=["Stock"])
        os.makedirs("output", exist_ok=True)
        df_out.to_csv(config.OUTPUT_FILE, index=False)
        print(f"\nSaved results to {config.OUTPUT_FILE}")
    else:
        print("\nNo stocks matched criteria.")


if __name__ == "__main__":
    main()