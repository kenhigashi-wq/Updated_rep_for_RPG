from faker import Faker
import random

fake = Faker()

races = ["Human", "Elf", "Dwarf", "Halfling"]
classes = ["Warrior", "Rogue", "Mage", "Cleric"]

def generate_name():
    return fake.first_name()

def generate_location():
    return fake.city()

def generate_backstory(name, race, char_class):
    return (
        f"{name} is a {race} {char_class} from the city of {generate_location()}. "
        f"They are known for being {fake.word()} and seek adventure to {fake.sentence().lower()}."
    )

def generate_random_identity():
    name = generate_name()
    race = random.choice(races)
    char_class = random.choice(classes)
    backstory = generate_backstory(name, race, char_class)

    return {
        "name": name,
        "race": race,
        "class": char_class,
        "backstory": backstory
    }