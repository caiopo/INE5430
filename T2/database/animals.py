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

# Diet
CARNIVORE = 'Carnivore'
HERBIVORE = 'Herbivore'
OMNIVORE = 'Omnivore'

IGNORE = 'ignore'

_animals = (
    ('Goldfish', FISH, ORANGE, SCALE, IGNORE, TINY,  OMNIVORE),
    ('Orca',     FISH, BLACK,  WET,   OCEAN,  LARGE, CARNIVORE),
    ('Salmon',   FISH, GREY,   SCALE, OCEAN,  SMALL, OMNIVORE),
    ('Shark',    FISH, GREY,   WET,   OCEAN,  LARGE, CARNIVORE),

    ('Frog', AMPHIBIAN, GREEN, WET, IGNORE, SMALL, CARNIVORE),

    ('Crocodile', REPTILE, GREEN, DRY,   IGNORE, LARGE, CARNIVORE),
    ('Turtle',    REPTILE, BROWN, SHELL, IGNORE, SMALL, OMNIVORE),

    ('Duck',   BIRD, IGNORE, FEATHER, IGNORE,  SMALL,  OMNIVORE),
    ('Eagle',  BIRD, BROWN,  FEATHER, AMERICA, MEDIUM, CARNIVORE),
    ('Falcon', BIRD, BROWN,  FEATHER, IGNORE,  SMALL,  CARNIVORE),
    ('Swan',   BIRD, WHITE,  FEATHER, AMERICA, IGNORE, OMNIVORE),

    ('Monkey',     MAMMAL, BROWN,  FUR, OCEAN,  LARGE,  OMNIVORE),
    ('Blue Whale', MAMMAL, GREY,   WET, OCEAN,  LARGE,  CARNIVORE),
    ('Cat',        MAMMAL, IGNORE, FUR, IGNORE, SMALL,  CARNIVORE),
    ('Cow',        MAMMAL, IGNORE, FUR, IGNORE, MEDIUM, CARNIVORE),
    ('Dog',        MAMMAL, IGNORE, FUR, IGNORE, SMALL,  CARNIVORE),
    ('Elephant',   MAMMAL, GREY,   DRY, AFRICA, LARGE,  HERBIVORE),
    ('Giraffe',    MAMMAL, BROWN,  FUR, AFRICA, LARGE,  HERBIVORE),
    ('Horse',      MAMMAL, IGNORE, FUR, IGNORE, MEDIUM, HERBIVORE),
    ('Lion',       MAMMAL, YELLOW, FUR, AFRICA, MEDIUM, CARNIVORE),
)


def load_animals(animals=_animals):
    for animal in animals:
        if Counter(animal)[IGNORE] > 2:
            raise ValueError(
                "can't have more than 2 ignores on the same animal")

    return pd.DataFrame(
        data=list(animals),
        columns=['name', 'type', 'color', 'skin_type',
                 'origin', 'size', 'diet'],
    )


load_animals().to_csv(path.join(BASE_DIR, 'animals.csv'))
