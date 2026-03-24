from flask import Flask, request, jsonify
import pandas as pd
import numpy as np
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


# route for task 2 Risk Metrics calulation
@app.route("/risk-metrics", methods=["POST"])
def risk_metrics():
    try:
        if "file" not in request.files:
            return jsonify({"error": "No file uploaded"}), 400

        file = request.files["file"]
        df = pd.read_csv(file)

        if "Returns" not in df.columns:
            return jsonify({"error": "CSV must contain 'Returns' column"}), 400

        returns = df["Returns"]

        # Calculate Sharpe Ratio
        sharpe = returns.mean() / returns.std()

        # Calculate  Volatility
        volatility = returns.std() * np.sqrt(252)

        # Calculate Maximum Drawdown
        cumulative = (1 + returns).cumprod()
        peak = cumulative.cummax()
        drawdown = (cumulative - peak) / peak
        max_dd = drawdown.min()

        return jsonify({
            "sharpe": round(float(sharpe), 4),
            "volatility": round(float(volatility), 4),
            "max_drawdown": round(float(max_dd), 4)
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# route for task 3 Time-Based strategy
@app.route("/strategy", methods=["POST"])
def strategy():
    try:
        if "file" not in request.files:
            return jsonify({"error": "No file uploaded"}), 400

        file = request.files["file"]
        df = pd.read_csv(file)

        required_cols = ["Date", "Close"]
        if not all(col in df.columns for col in required_cols):
            return jsonify({"error": "CSV must contain Date and Close columns"}), 400


        df["Date"] = pd.to_datetime(df["Date"])
        df = df.sort_values(by="Date")
        df["Day"] = df["Date"].dt.day_name()

        trades = []
        buy_price = None

        for i in range(len(df)):
            row = df.iloc[i]

            # Buy stockes only on  Monday
            if row["Day"] == "Monday":
                buy_price = row["Close"]

            # sell only on Friday
            elif row["Day"] == "Friday" and buy_price is not None:
                sell_price = row["Close"]
                profit = round(float(sell_price - buy_price), 2)

                trades.append({
                    "Buy": round(float(buy_price), 2),
                    "Sell": round(float(sell_price), 2),
                    "Profit": profit
                })

                buy_price = None

        total_profit = round(sum(t["Profit"] for t in trades), 2)

        return jsonify({
            "trades": trades,
            "total_profit": total_profit
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)