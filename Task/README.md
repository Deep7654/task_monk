# Stock Analysis and UI Representation

This repository contains two main components:
1. **UIRepresentation**: A web-based graphical interface running via Docker.
2. **Code**: Python scripts for stock analysis tasks (Screener, Risk Metrics, Strategy).

---

## 🖥️ UI Representation

To view the visual UI representation of the project:

1. Navigate to the UI folder:
   ```bash
   cd UIRepresentation
   ```

2. Build and run the Docker containers:
   ```bash
   docker-compose up --build
   ```

3. Open your browser and navigate to `http://localhost:5173`. 
   *(Note: If port 5173 is busy, try `http://localhost:5174`)*

### How to use the UI:
- **Risk Metrics**: Upload the `return.csv` file.
- **Stock Strategy**: Upload a CSV file containing stock `Close` prices for all days (specifically ensure data for Monday and Friday is present).

eg - 

```Date,Open,High,Low,Close,Volume
2024-01-01,141.15,141.52,140.75,141.28,34384
2024-01-02,141.37,141.96,140.87,141.92,17669
2024-01-03,142.1,143.81,141.86,142.97,25565
2024-01-04,144.9,145.14,144.13,144.66,19405
2024-01-05,142.96,144.49,142.34,143.49,27431
```

---

## ⚙️ Terminal View (Code/Tasks)

The code for the three main tasks is located in `Code/stock-analysis/tasks`. 

To run the scripts manually in the terminal:

1. Navigate to the root folder of the stock analysis code:
   ```bash
   cd Code/stock-analysis
   ```

2. Start and activate your Python virtual environment (`venv`).
   - Windows: .\venv\Scripts\activate
   - Mac/Linux: source venv/bin/activate

3. Install the required packages (if they aren't installed already):
   ```bash
   python -m pip install -r requirements.txt
   ```

### Running the Tasks

Ensure you are in the `stock-analysis` root directory, and run the tasks as Python modules to avoid import path issues:

- **Task 1: Stock Screener**
  ```bash
  python -m tasks.task1_screener
  ```
  *(The selected stocks output will be stored in the `output/` folder).*

- **Task 2: Risk Metrics**
  ```bash
  python -m tasks.task2_risk
  ```

- **Task 3: Stock Strategy**
  ```bash
  python -m tasks.task3_strategy
  ```

### Data Configuration
- All input data should be placed in the `data/` directory.
- **Task 2 (Risk)** uses `data/returns.csv` as its input.
- **Tasks 1 & 3** use the data CSVs available in the `data/` folder according to your choice (such as the daily stock price data).
