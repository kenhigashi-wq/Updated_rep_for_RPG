from faker import Faker
import random

class RandomGenerator:
    def __init__(self):
        self.fake = Faker()
        self.races = ["Human", "Elf", "Dwarf", "Halfling"]
        self.classes = ["Warrior", "Mage", "Rogue", "Cleric"]

    def generate_character(self):
        name = self.fake.first_name()
        race = random.choice(self.races)
        char_class = random.choice(self.classes)
        backstory = f"{name} is a {race} {char_class} from {self.fake.city()}."

        return {
            "name": name,
            "race": race,
            "class": char_class,
            "backstory": backstory
        }