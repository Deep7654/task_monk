import { useState } from "react";
import axios from "axios";

type RiskResult = {
  sharpe: number;
  volatility: number;
  max_drawdown: number;
};

export default function Task2() {
  const [file, setFile] = useState<File | null>(null);
  const [result, setResult] = useState<RiskResult | null>(null);

  const handleUpload = async () => {
    if (!file) return alert("Upload CSV first");

    const formData = new FormData();
    formData.append("file", file);

    const res = await axios.post<RiskResult>(
      "http://localhost:5000/risk-metrics",
      formData
    );

    setResult(res.data);
  };

  return (
    <div>
      <h1>Risk Metrics</h1>

      <input
        type="file"
        onChange={(e: React.ChangeEvent<HTMLInputElement>) => {
          if (e.target.files) setFile(e.target.files[0]);
        }}
      />

      <button onClick={handleUpload}>Anlyze</button>

      {result && (
        <div className="result">
          <p>Sharpe Ratio: {result.sharpe}</p>
          <p>Volatility: {result.volatility}</p>
          <p>Max Drawdown: {result.max_drawdown}</p>
        </div>
      )}
    </div>
  );
}