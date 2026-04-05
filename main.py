# main.py

import char_making
from random_generator import RandomGenerator
from data_analysis import StatisticalAnalyzer
from visualization import DataVisualization

characters = {}  
stats = {}        

rg = RandomGenerator()


def pause():
    input("\nPress Enter to continue...")


def create_character():
    choice = input("Generate random character? (y/n): ").lower()

    if choice == "y":
        data = rg.generate_character()
        name = data["name"]
        race = data["race"]
        char_class = data["class"]

        print("\nGenerated Character")
        print(data["backstory"])
    else:
        name = input("Enter name: ")
        race = input("Enter race: ")
        char_class = input("Enter class: ")

    stats_dict = char_making.roll_stats()
    character = char_making.Character(name, race, char_class, stats_dict)

    characters[name] = character
    stats[name] = character.to_dict()

    print(f"\nCharacter '{name}' created.")
    pause()


def random_generator_menu():
    data = rg.generate_character()
    print("\nRandom Character Template")
    print(f"Name: {data['name']}")
    print(f"Race: {data['race']}")
    print(f"Class: {data['class']}")
    print(f"Backstory: {data['backstory']}")
    pause()



def character_visualization_menu():
    if not stats:
        print("No characters available.")
        pause()
        return

    analyzer = StatisticalAnalyzer(stats)
    df = analyzer.get_dataframe()
    viz = DataVisualization(df)

    print("\nSelect character:")
    for i, name in enumerate(stats.keys(), start=1):
        print(f"[{i}] {name}")

    choice = input("Enter choice: ")

    if not choice.isdigit():
        print("Invalid input.")
        pause()
        return

    index = int(choice) - 1
    names = list(stats.keys())

    if index < 0 or index >= len(names):
        print("Invalid selection.")
        pause()
        return

    viz.character_bar_chart(names[index])
    pause()


def statistical_analysis_menu():
    if not stats:
        print("No characters available.")
        pause()
        return

    analyzer = StatisticalAnalyzer(stats)
    results = analyzer.analyze()

    print("\nStatistical Analysis")
    print("\nMean:")
    print(results["mean"])
    print("\nMinimum:")
    print(results["min"])
    print("\nMaximum:")
    print(results["max"])
    pause()


def character_comparison_menu():
    if not stats:
        print("No characters available.")
        pause()
        return

    analyzer = StatisticalAnalyzer(stats)
    df = analyzer.get_dataframe()

    print("Available stats:")
    for col in df.columns:
        print(f"- {col}")

    stat = input("Enter stat to compare: ").lower()
    if stat not in df.columns:
        print("Invalid stat.")
        pause()
        return

    df[stat].plot(kind="bar", title=f"Comparison by {stat}")
    pause()



def export_character_data():
    if not stats:
        print("No characters available.")
        pause()
        return

    analyzer = StatisticalAnalyzer(stats)
    analyzer.export_csv()
    print("Character data exported to CSV.")
    pause()


def import_character_data():
    global stats, characters

    try:
        df = StatisticalAnalyzer.import_csv()
        stats.clear()
        characters.clear()

        for name, row in df.iterrows():
            stats[name] = row.to_dict()
            characters[name] = char_making.Character(
                name, "Unknown", "Unknown", row.to_dict()
            )

        print("Character data imported from CSV.")
    except FileNotFoundError:
        print("No CSV file found.")
    pause()




def main_menu():
    while True:
        print("\nUpgraded RPG manager\n")

        print("data & analysis:")
        print("[1] Character Visualization")
        print("[2] Statistical Analysis")
        print("[3] Character Comparison Tools")

        print("\character futures:")
        print("[4] Create Character")
        print("[5] Random Generator")

        print("\nData Management:")
        print("[6] Export Character Data")
        print("[7] Import Character Data")

        print("\n[Q] Quit")

        choice = input("\nEnter your choice: ").lower()

        if choice == "1":
            character_visualization_menu()
        elif choice == "2":
            statistical_analysis_menu()
        elif choice == "3":
            character_comparison_menu()
        elif choice == "4":
            create_character()
        elif choice == "5":
            random_generator_menu()
        elif choice == "6":
            export_character_data()
        elif choice == "7":
            import_character_data()
        elif choice == "q":
            break
        else:
            print("Invalid choice")


main_menu()