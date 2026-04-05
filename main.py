#KH Main
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
        name = input("Enter name: ")
        race = input("Enter race: ")
        char_class = input("Enter class: ")

    stats[name] = char_making.roll_stats()
    inventories[name] = []
    names.append(name)

    print(f"\nCharacter '{name}' created successfully.")
    pause()

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
        name = input("Enter name: ")
        race = input("Enter race: ")
        char_class = input("Enter class: ")

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

#test
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


def main_menu():
    while True:
        print("\nRPG manager")
        print("\nData and analysis:")
        print("[1] Character Visualization")
        print("[2] Statistical Analysis")

        print("\nCHARACTER FEATURES:")
        print("[3] Create Character")
        print("[4] Random Generator")

        print("\nDATA MANAGEMENT:")
        print("[6] Import Character Data")
        print("[5] Export Character Data")

        print("\n[Q] Quit")

        choice = input("\nEnter your choice: ").lower()

        if choice == "1":
            visualization_menu()
        elif choice == "2":
            statistical_analysis_menu()
        elif choice == "3":
            create_character()
        elif choice == "4":
            character = rg.generate_random_identity()
            print(character["backstory"])
            pause()
        elif choice == "5":
            export_character_data()
        elif choice == "6":
            import_character_data()
        elif choice == "q":
            break
        else:
            print("Invalid option.")

def import_character_data():
    global stats

    try:
        df = da.import_csv()
        stats.clear()

        for name, row in df.iterrows():
            stats[name] = row.to_dict()

        print("Character data imported successfully from CSV.")
    except FileNotFoundError:
        print("No CSV file found. Export data first.")
    pause()

main_menu()

