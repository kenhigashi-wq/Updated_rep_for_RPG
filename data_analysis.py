#KH data stuff with panda, UPDATED

import pandas as pd

def build_character_dataframe(stats_dict):

    df = pd.DataFrame.from_dict(stats_dict, orient="index")
    df.index.name = "Character"
    return df


def analyze_stats(df):

    analysis = {
        "mean": df.mean(),
        "min": df.min(),
        "max": df.max()
    }
    return analysis


def export_to_csv(df, filename="character_stats.csv"):
    df.to_csv(filename)
    print(f"Character data exported to {filename}")


def load_from_csv(filename="character_stats.csv"):
    df = pd.read_csv(filename, index_col="Character")
    print(f"Character data loaded from {filename}")
    return df

def import_csv(filename="character_data.csv"):
    return pd.read_csv(filename, index_col=0)