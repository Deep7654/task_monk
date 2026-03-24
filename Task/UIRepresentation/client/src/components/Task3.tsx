import { useState } from "react";
import axios from "axios";

type Trade = {
  Buy: number;
  Sell: number;
  Profit: number;
};

type StrategyResult = {
  trades: Trade[];
  total_profit: number;
};

export default function Task3() {
  const [file, setFile] = useState<File | null>(null);
  const [result, setResult] = useState<StrategyResult | null>(null);

  const handleUpload = async () => {
    if (!file) return alert("Upload CSV first");

    const formData = new FormData();
    formData.append("file", file);

    const res = await axios.post<StrategyResult>(
      "http://localhost:5000/strategy",
      formData
    );

    setResult(res.data);
  };

  return (
    <div >
      <h1>Stock Strategy</h1>
      {/* <label>Upload CSV with columns: Date, Open, High, Low, Close</label> */}
      <input
        type="file"
        onChange={(e: React.ChangeEvent<HTMLInputElement>) => {
          if (e.target.files) setFile(e.target.files[0]);
        }}
      />
      <button onClick={handleUpload}>Run Strategy</button>

      {result && (
        <div className="result">
          {result.trades.map((t, i) => (
            <p key={i}>
              Buy: {t.Buy} | Sell: {t.Sell} | Profit: {t.Profit}
            </p>
          ))}

          <h3>Total Profit: {result.total_profit}</h3>
        </div>
      )}
    </div>
  );
}