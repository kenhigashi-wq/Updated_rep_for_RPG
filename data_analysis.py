import pandas as pd

class StatisticalAnalyzer:
    def __init__(self, stats_dict):
        self.df = pd.DataFrame.from_dict(stats_dict, orient="index")

    def basic_analysis(self):
        return {
            "mean": self.df.mean(),
            "min": self.df.min(),
            "max": self.df.max()
        }

    def export_csv(self, filename="character_data.csv"):
        self.df.to_csv(filename)

    def import_csv(self, filename="character_data.csv"):
        return pd.read_csv(filename, index_col=0)