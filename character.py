class Character:
    def __init__(self, name, race, char_class, stats):
        self.name = name
        self.race = race
        self.char_class = char_class
        self.stats = stats

    def to_dict(self):
        return self.stats