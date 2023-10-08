class Pokemon(object):
    attack = 12
    defense = 10
    health = 15
    p_type = "Normal"

    def __init__(self, name, level=5):
        self.evolve = None
        self.defense_boost = None
        self.attack_boost = None
        self.health_boost = None
        self.name = name
        self.level = level

    def train(self):
        self.update()
        self.attack_up()
        self.defense_up()
        self.health_up()
        self.level = self.level + 1
        if self.level % self.evolve == 0:
            return self.level, "Evolved!"
        else:
            return self.level

    def attack_up(self):
        self.attack = self.attack + self.attack_boost
        return self.attack

    def defense_up(self):
        self.defense = self.defense + self.defense_boost
        return self.defense

    def health_up(self):
        self.health = self.health + self.health_boost
        return self.health

    def update(self):
        self.health_boost = 5
        self.attack_boost = 3
        self.defense_boost = 2
        self.evolve = 10

    def opponent(self):
        if self.p_type == 'Grass':
            return ('Fire', 'Water')

        if self.p_type == 'Ghost':
            return ('Dark', 'Psychic')

        if self.p_type == 'Fire':
            return ('Water', 'Grass')

        if self.p_type == 'Flying':
            return ('Electric', 'Fighting')

    def __str__(self):
        self.update()
        return "Pokemon name: {}, Type: {}, Level: {}, Attack: {}".format(self.name, self.p_type, self.level,
                                                                          self.attack)


class Grass_Pokemon(Pokemon):
    attack = 15
    defense = 14
    health = 12
    p_type = 'Grass'

    def __init__(self, name, level=5):
        super().__init__(name, level)
        self.evolve = None
        self.defense_boost = None
        self.attack_boost = None
        self.health_boost = None
        self.p_moves = None

    def train(self):
        self.update()
        self.defense_up()
        self.health_up()
        self.level = self.level + 1

        if self.level >= 10:
            self.attack = self.attack + self.attack_boost

        if self.level % self.evolve == 0:
            return self.level, "Evolved!"
        else:
            return self.level

    def update(self):
        self.health_boost = 6
        self.attack_boost = 2
        self.defense_boost = 3
        self.evolve = 12

    def moves(self):
        self.p_moves = ["razor leaf", "synthesis", "petal dance", "petal blizzard"]

    def action(self):
        return '{} knows a lot of different moves!'.format(self.name)


p1 = Grass_Pokemon('Belle')
p2 = Grass_Pokemon('Bulby')
p3 = Grass_Pokemon('Pika')

print(p2)
p2.train()
p2.train()
p2.train()
p2.train()
p2.train()
print(p2)

print(p3)
p3.train()
p3.train()
p3.train()
p3.train()
p3.train()
print(p3)
