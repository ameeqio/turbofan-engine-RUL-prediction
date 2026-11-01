from __future__ import annotations
import pandas as pd
from pathlib import Path
from src.config import TRAIN_DATA_PATH, TEST_DATA_PATH, RUL_DATA_PATH, COLUMN_NAMES

class DataLoader:
    def __init__(self)-> None:
        self.train_data_path: Path = TRAIN_DATA_PATH
        self.test_data_path: Path = TEST_DATA_PATH
        self.rul_data_path: Path = RUL_DATA_PATH

    def load_data(self)-> pd.DataFrame:
        train_data: pd.DataFrame = pd.read_csv(
            filepath_or_buffer = self.train_data_path,
            sep = r"\s+",
            header = None,
            names = COLUMN_NAMES
        )

        test_Data: pd.DataFrame = pd.read_csv(
            filepath_or_buffer = self.test_data_path,
            sep = r"\s+",
            header = None,
            names = COLUMN_NAMES
        )

        rul_data: pd.DataFrame = pd.read_csv(
            filepath_or_buffer = RUL_DATA_PATH,
            sep = r"\s+",
            header = None,
            names = ["RUL"]
        )

        return train_data, test_Data, rul_data

    