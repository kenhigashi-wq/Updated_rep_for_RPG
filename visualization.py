# visualization.py

import matplotlib.pyplot as plt

class DataVisualization:
    def __init__(self, dataframe):
        self.df = dataframe

    def character_bar_chart(self, character_name):
        if character_name not in self.df.index:
            print("Character not found")
            return

        self.df.loc[character_name].plot(kind="bar")
        plt.title(f"{character_name} - Character Stats")
        plt.xlabel("Attributes")
        plt.ylabel("Valuue")
        plt.tight_layout()
        plt.show()