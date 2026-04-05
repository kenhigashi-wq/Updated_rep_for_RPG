# data_analysis.py

import pandas as pd

class StatisticalAnalyzer:
    def __init__(self, character_dict):

        self.df = pd.DataFrame.from_dict(character_dict, orient="index")

    def get_dataframe(self):
        return self.df

    def analyze(self):
        return {
            "mean": self.df.mean(),
            "min": self.df.min(),
            "max": self.df.max()
        }

    def export_csv(self, filename="character_data.csv"):
        self.df.to_csv(filename)

    @staticmethod
    def import_csv(filename="character_data.csv"):
        return pd.read_csv(filename, index_col=0)