import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FOLDER = os.path.join(BASE_DIR, "data")
OUTPUT_FILE = os.path.join(BASE_DIR, "output", "results.csv")
MOVING_AVG_WINDOW = 50
VOLUME_LOOKBACK = 5