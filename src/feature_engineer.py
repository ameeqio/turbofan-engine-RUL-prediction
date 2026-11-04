from __future__ import annotations
import pandas as pd
import numpy as np

class FeatureEngineerRUL:
    def __init__(self, train_data: pd.DataFrame, test_data: pd.DataFrame, rul_data: pd.Series)-> None:
        self.train_data = train_data
        self.test_data = test_data
        self.rul_data = rul_data

    def engineer(self)-> pd.DataFrame:
        # rul target variable engineering for the test data
        test_engine_last_cycles: pd.Series = self.test_data.groupby(by = "engine_id")["cycle"].max()
        self.test_data["last_cycle"] = self.test_data["engine_id"].map(test_engine_last_cycles)

        rul_engines_from_last_cycles: pd.Series = pd.Series(
            self.rul_data['RUL'].to_numpy(),
            index = [i for i in range(1, 249)]
        )

        self.test_data["RUL_from_last_cycle"] = self.test_data["engine_id"].map(rul_engines_from_last_cycles)

        self.test_data["max_cycles"] = self.test_data["last_cycle"] + self.test_data["RUL_from_last_cycle"]
        self.test_data["RUL"] = self.test_data["max_cycles"] - self.test_data["cycle"]

        self.test_data.drop(columns = ['last_cycle', 'RUL_from_last_cycle', 'max_cycles'], inplace = True)

        # rul target variable engineering for the train data
        self.train_data["RUL"] = self.train_data.groupby(by = "engine_id")["cycle"].transform("max") - self.train_data["cycle"]

        return self.train_data, self.test_data, self.rul_data