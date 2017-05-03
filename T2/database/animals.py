import pandas as pd

from os import path
from properties import Colors, SkinTypes, Origins, Size
from collections import Counter

BASE_DIR = path.dirname(path.abspath(__file__))

# Type
FISH = 'Fish'
AMPHIBIAN = 'Amphibian'
REPTILE = 'Reptile'
BIRD = 'Bird'
MAMMAL = 'Mammal'

# Colors
BLACK = 'Black'
BLUE = 'Blue'
BROWN = 'Brown'
GREEN = 'Green'
GREY = 'Grey'
ORANGE = 'Orange'
PINK = 'Pink'
PURPLE = 'Purple'
RED = 'Red'
WHITE = 'White'
YELLOW = 'Yellow'

# Skin types
DRY = 'Dry'
FEATHER = 'Feather'
FUR = 'Fur'
SCALE = 'Scale'
SHELL = 'Shell'
WET = 'Wet'

# Locations
AFRICA = 'Africa'
AMERICA = 'America'
ASIA = 'Asia'
EUROPE = 'Europe'
OCEAN = 'Ocean'
OCEANIA = 'Oceania'
POLES = 'North/South Pole'

# Sizes
# TINY = '< 10 cm'
# SMALL = '10 cm to 1 m'
# MEDIUM = '1 m to 2 m'
# LARGE = '> 2 m'
TINY = 'Tiny'
SMALL = 'Small'
MEDIUM = 'Medium'
LARGE = 'Large'

IGNORE = 'ignore'


def load_animals():
    animals = []

    def insert(name, type_, color, skin_type, origin, size):
        animal = {
            'name': name,
            'type': type_,
            'color': color,
            'skin_type': skin_type,
            'origin': origin,
            'size': size,
        }

        if Counter(animal.values())[IGNORE] > 2:
            raise ValueError(
                "can't have more than 2 ignores on the same animal")

        animals.append(animal)

    insert('Goldfish', FISH, ORANGE, SCALE, IGNORE, TINY)
    insert('Orca', FISH, BLACK, WET, OCEAN, LARGE)
    insert('Salmon', FISH, GREY, SCALE, OCEAN, SMALL)
    insert('Shark', FISH, GREY, WET, OCEAN, LARGE)

    insert('Frog', AMPHIBIAN, GREEN, WET, IGNORE, SMALL)

    insert('Crocodile', REPTILE, GREEN, DRY, IGNORE, LARGE)
    insert('Turtle', REPTILE, BROWN, SHELL, IGNORE, SMALL)

    insert('Duck', BIRD, IGNORE, FEATHER, IGNORE, SMALL)
    insert('Eagle', BIRD, BROWN, FEATHER, AMERICA, MEDIUM)
    insert('Falcon', BIRD, BROWN, FEATHER, IGNORE, SMALL)
    insert('Swan', BIRD, WHITE, FEATHER, AMERICA, IGNORE)

    insert('Monkey', MAMMAL, BROWN, FUR, OCEAN, LARGE)
    insert('Blue Whale', MAMMAL, GREY, WET, OCEAN, LARGE)
    insert('Cat', MAMMAL, IGNORE, FUR, IGNORE, SMALL)
    insert('Cow', MAMMAL, IGNORE, FUR, IGNORE, MEDIUM)
    insert('Dog', MAMMAL, IGNORE, FUR, IGNORE, SMALL)
    insert('Elephant', MAMMAL, GREY, DRY, AFRICA, LARGE)
    insert('Giraffe', MAMMAL, BROWN, FUR, AFRICA, LARGE)
    insert('Horse', MAMMAL, IGNORE, FUR, IGNORE, MEDIUM)
    insert('Lion', MAMMAL, YELLOW, FUR, AFRICA, MEDIUM)

    return pd.DataFrame(
        data=animals,
        columns=['name', 'type', 'color', 'skin_type', 'origin', 'size'],
    )

# load_animals().to_csv(path.join(BASE_DIR, 'animals.csv'))
