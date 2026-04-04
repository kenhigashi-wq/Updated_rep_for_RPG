import matplotlib.pyplot as plt

def character_bar_chart(df, character_name):

    if character_name not in df.index:
        print("Character not found.")
        return

    stats = df.loc[character_name]

    plt.figure()
    stats.plot(kind="bar")
    plt.title(f"{character_name} - Character Stats")
    plt.xlabel("Attributes")
    plt.ylabel("Value")
    plt.tight_layout()
    plt.show()