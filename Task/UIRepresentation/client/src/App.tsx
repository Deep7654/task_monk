import { useState } from "react";
import Task2 from "./components/Task2";
import Task3 from "./components/Task3";
import "./App.css";

export default function App() {
  const [activeTab, setActiveTab] = useState<"task2" | "task3">("task2");

  return (
    <div className="container">
      <h1>Stock Dashboard</h1>

      <div className="tabs">
        <button
          className={activeTab === "task2" ? "active" : ""}
          onClick={() => setActiveTab("task2")}
        >
          Task 2
        </button>

        <button
          className={activeTab === "task3" ? "active" : ""}
          onClick={() => setActiveTab("task3")}
        >
          Task 3
        </button>
      </div>

      <div className="card">
        {activeTab === "task2" && <Task2 />}
        {activeTab === "task3" && <Task3 />}
      </div>
    </div>
  );
}