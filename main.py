#KH
import char_making
import deaninventory
import pakistans_functions as pf
import data_analysis as da
import visualization as vz
import random_generator as rg



stats = {}
inventories = {}
names = []



def pause():
    input("\nPress Enter to continue...")



def create_character():
    choice = input("Generate random character? (y/n): ").lower()

    if choice == "y":
        character = rg.generate_random_identity()
        name = character["name"]
        race = character["race"]
        char_class = character["class"]

        print("\nGenerated Character")
        print(f"Name: {name}")
        print(f"Race: {race}")
        print(f"Class: {char_class}")
        print(f"Backstory: {character['backstory']}")
    else:
        name, race, char_class = char_making.make_character()

    stats[name] = char_making.roll_stats()
    inventories[name] = []
    names.append(name)

    print(f"\nCharacter '{name}' created successfully.")
    pause()



def character_visualization():
    if not stats:
        print("No characters available.")
        pause()
        return

    df = da.build_dataframe(stats)

    print("\nSelect character for detailed visualization:")
    name_list = list(stats.keys())
    for i, name in enumerate(name_list, start=1):
        print(f"[{i}] {name}")

    choice = input("Enter choice: ")

    if not choice.isdigit():
        print("Invalid input.")
        pause()
        return

    index = int(choice) - 1
    if index < 0 or index >= len(name_list):
        print("Invalid selection.")
        pause()
        return

    selected_name = name_list[index]
    print(f"\nGenerating character profile for {selected_name}...")

    vz.character_bar_chart(df, selected_name)
    pause()


def visualization_menu():
    while True:
        print("\nCharacter vizulation")

        print(f"Current Characters: {len(stats)} total\n")

        print("visualization  options:")
        print("[A] Individual Character Stat Chart")
        print("[M] Main Menu")

        choice = input("\nEnter your choice: ").lower()

        if choice == "a":
            character_visualization()
        elif choice == "m":
            return
        else:
            print("Invalid option.")


def statistical_analysis_menu():
    if not stats:
        print("No characters available.")
        pause()
        return

    df = da.build_dataframe(stats)
    analysis = da.basic_analysis(df)

    print("\nStatistical analysis")
    print("\nCharacter Data:")
    print(df)

    print("\nMean:")
    print(analysis["mean"])

    print("\nMinimum:")
    print(analysis["min"])

    print("\nMaximum:")
    print(analysis["max"])

    pause()


def export_character_data():
    if not stats:
        print("No characters available.")
        pause()
        return

    df = da.build_dataframe(stats)
    da.export_csv(df)
    pause()


