from __future__ import annotations
from pathlib import Path

# PROJECT ROOT DIRECTORY
ROOT_DIR: Path = Path(__file__).resolve().parent.parent

# DATA DIRECTORY
DATA_DIR: Path = ROOT_DIR / "data" / "raw"
DATASET: str = "FD004"

# DATASET 
TRAIN_DATA_PATH: Path = DATA_DIR / f"train_{DATASET}.txt"
TEST_DATA_PATH: Path = DATA_DIR / f"test_{DATASET}.txt"
RUL_DATA_PATH: Path = DATA_DIR / f"RUL_{DATASET}.txt"

# COLUMNS
COLUMN_NAMES: list[str] = (
    ["engine_id", "cycle"] + [f"setting_{i}" for i in range(1, 4)] + [f"sensor_{i}" for i in range(1, 22)]
)

SETTING_COLS: list[str] = [f"setting_{i}" for i in range(1, 4)]
SENSOR_COLS: list[str] = [f"sensor_{i}" for i in range(1, 22)]




