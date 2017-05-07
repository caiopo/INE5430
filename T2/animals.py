import pandas as pd

from os import path
from collections import Counter


BASE_DIR = path.dirname(path.abspath(__file__))

# Type
FISH = 'Peixe'
AMPHIBIAN = 'Anfíbio'
REPTILE = 'Reptil'
BIRD = 'Pássaro'
MAMMAL = 'Mamífero'

# Colors
BLACK = 'Preto'
BLUE = 'Azul'
BROWN = 'Marrom'
GREEN = 'Verde'
GREY = 'Cinza'
ORANGE = 'Laranja'
PINK = 'Rosa'
PURPLE = 'Roxo'
RED = 'Vermelho'
WHITE = 'Branco'
YELLOW = 'Amarelo'

# Skin types
DRY = 'Couro'
FEATHER = 'Penas'
FUR = 'Pêlo'
SCALE = 'Escamas'
SHELL = 'Casco'
WET = 'Úmida'

# Habitat
DESERT = 'Deserto'
FRESHWATER = 'Água Doce'
GRASSLAND = 'Planície'
MOUNTAIN = 'Montanha'
OCEAN = 'Oceano'
POLAR = 'Pólo Norte/Sul'
SWAMP = 'Pântano'
FOREST = 'Floresta'
URBAN = 'Urbano'

# Sizes
# TINY = '< 10 cm'
# SMALL = '10 cm to 1 m'
# MEDIUM = '1 m to 2 m'
# LARGE = '> 2 m'
TINY = 'Muito pequeno'
SMALL = 'Pequeno'
MEDIUM = 'Médio'
LARGE = 'Grande'

# Diet
CARNIVORE = 'Carnívoro'
HERBIVORE = 'Herbívoro'
OMNIVORE = 'Onívoro'

IGNORE = 'ignore'

YES = True
NO = False


# burro
# capivara
# cervo
# chipanze
# esquilo
# guaxinim
# gorila
# hiena
# iguana
# jaguatirica
# lemure
# lontra
# onca
# quati
# tamanduá


_animals = (
    ('Boto',             FISH, PINK,   WET,   OCEAN,      MEDIUM, CARNIVORE, IGNORE),
    ('Cavalo Marinho',   FISH, IGNORE, WET,   OCEAN,      TINY,   CARNIVORE, NO),
    ('Golfinho',         FISH, GREY,   WET,   OCEAN,      LARGE,  CARNIVORE, IGNORE),
    ('Orca',             FISH, BLACK,  WET,   OCEAN,      LARGE,  CARNIVORE, YES),
    ('Peixinho-dourado', FISH, ORANGE, SCALE, FRESHWATER, TINY,   OMNIVORE,  NO),
    ('Piranha',          FISH, GREY,   WET,   FRESHWATER,      SMALL,  CARNIVORE, YES),
    ('Salmão',           FISH, GREY,   SCALE, OCEAN,      SMALL,  OMNIVORE,  NO),
    ('Tainha',           FISH, GREY,   WET,   OCEAN,      SMALL,  OMNIVORE,  NO),
    ('Tubarão',          FISH, GREY,   WET,   OCEAN,      LARGE,  CARNIVORE, YES),

    ('Pereca',     AMPHIBIAN, GREEN, WET, FOREST, SMALL, CARNIVORE, NO),
    ('Rã',         AMPHIBIAN, BROWN, WET, FOREST, SMALL, CARNIVORE, NO),
    ('Rã',         AMPHIBIAN, GREEN, WET, FOREST, SMALL, CARNIVORE, NO),
    ('Salamandra', AMPHIBIAN, GREEN, WET, FOREST, SMALL, CARNIVORE, IGNORE),
    ('Sapo',       AMPHIBIAN, GREEN, WET, FOREST, SMALL, CARNIVORE, NO),

    ('Cobra',     REPTILE, BROWN,  DRY,   FOREST, LARGE, CARNIVORE, YES),
    ('Crocodilo', REPTILE, GREEN,  DRY,   SWAMP,  LARGE, CARNIVORE, YES),
    ('Jacaré',    REPTILE, GREEN,  DRY,   SWAMP,  LARGE, CARNIVORE, YES),
    ('Lagarto',   REPTILE, IGNORE, SCALE, FOREST, SMALL, OMNIVORE,  NO),
    ('Tartaruga', REPTILE, BROWN,  SHELL, OCEAN,  SMALL, OMNIVORE,  NO),

    ('Águia',    BIRD, BROWN,  FEATHER, IGNORE,  MEDIUM, CARNIVORE, YES),
    ('Avestruz', BIRD, WHITE,  FEATHER, IGNORE,  LARGE,  OMNIVORE,  NO),
    ('Cisne',    BIRD, WHITE,  FEATHER, IGNORE,  SMALL,  OMNIVORE,  NO),
    ('Coruja',   BIRD, WHITE,  FEATHER, FOREST,  SMALL,  OMNIVORE,  NO),
    ('Corvo',    BIRD, BLACK,  FEATHER, IGNORE,  SMALL,  OMNIVORE,  NO),
    ('Ema',      BIRD, WHITE,  FEATHER, IGNORE,  LARGE,  OMNIVORE,  NO),
    ('Falcão',   BIRD, BROWN,  FEATHER, IGNORE,  SMALL,  CARNIVORE, YES),
    ('Flamingo', BIRD, PINK,   FEATHER, IGNORE,  MEDIUM, CARNIVORE, NO),
    ('Gaivota',  BIRD, IGNORE, FEATHER, IGNORE,  SMALL,  CARNIVORE, NO),
    ('Galinha',  BIRD, BROWN,  FEATHER, URBAN,   SMALL,  OMNIVORE,  NO),
    ('Gaviao',   BIRD, WHITE,  FEATHER, IGNORE,  MEDIUM, OMNIVORE,  YES),
    ('Papagaio', BIRD, GREEN,  FEATHER, FOREST,  SMALL,  HERBIVORE, NO),
    ('Pato',     BIRD, IGNORE, FEATHER, IGNORE,  SMALL,  OMNIVORE,  NO),
    ('Picapau',  BIRD, WHITE,  FEATHER, IGNORE,  SMALL,  OMNIVORE,  NO),
    ('Pinguim',  BIRD, BLACK,  FEATHER, POLAR,   MEDIUM, OMNIVORE,  NO),
    ('Tucano',   BIRD, BLACK,  FEATHER, FOREST,  MEDIUM, OMNIVORE,  NO),

    ('Alpaca',       MAMMAL, IGNORE, FUR,    MOUNTAIN,  MEDIUM, HERBIVORE, NO),
    ('Anta',         MAMMAL, GREY,   FUR,    FOREST,    MEDIUM, HERBIVORE, NO),
    ('Baleia',       MAMMAL, GREY,   WET,    OCEAN,     LARGE,  CARNIVORE, YES),
    ('Cachorro',     MAMMAL, IGNORE, FUR,    URBAN,     SMALL,  CARNIVORE, NO),
    ('Camelo',       MAMMAL, YELLOW, FUR,    DESERT,    MEDIUM, HERBIVORE, NO),
    ('Canguru',      MAMMAL, BROWN,  FUR,    GRASSLAND, MEDIUM, HERBIVORE, NO),
    ('Cavalo',       MAMMAL, IGNORE, FUR,    GRASSLAND, MEDIUM, HERBIVORE, NO),
    ('Coelho',       MAMMAL, GREY,   FUR,    IGNORE,    MEDIUM, HERBIVORE, NO),
    ('Elefante',     MAMMAL, GREY,   DRY,    GRASSLAND, LARGE,  HERBIVORE, IGNORE),
    ('Foca',         MAMMAL, GREY,   FUR,    POLAR,     MEDIUM, CARNIVORE, IGNORE),
    ('Gato',         MAMMAL, IGNORE, FUR,    URBAN,     SMALL,  CARNIVORE, NO),
    ('Girafa',       MAMMAL, BROWN,  FUR,    GRASSLAND, LARGE,  HERBIVORE, NO),
    ('Hipopótamo',   MAMMAL, BROWN,  WET,    IGNORE,    LARGE,  HERBIVORE, YES),
    ('Humano',       MAMMAL, IGNORE, IGNORE, FOREST,    MEDIUM, OMNIVORE,  YES),
    ('Leão Marinho', MAMMAL, GREY,   DRY,    POLAR,     MEDIUM, CARNIVORE, IGNORE),
    ('Leão',         MAMMAL, YELLOW, FUR,    GRASSLAND, MEDIUM, CARNIVORE, YES),
    ('Lobo',         MAMMAL, GREY,   FUR,    FOREST,    MEDIUM, CARNIVORE, YES),
    ('Macaco',       MAMMAL, BROWN,  FUR,    FOREST,    LARGE,  OMNIVORE,  NO),
    ('Morcego',      MAMMAL, BLACK,  FUR,    IGNORE,    SMALL,  OMNIVORE,  NO),
    ('Onitorrinco',  MAMMAL, BROWN,  FUR,    IGNORE,    SMALL,  CARNIVORE, IGNORE),
    ('Ovelha',       MAMMAL, WHITE,  FUR,    GRASSLAND, MEDIUM, HERBIVORE, NO),
    ('Porco',        MAMMAL, PINK,   FUR,    URBAN,     MEDIUM, OMNIVORE,  NO),
    ('Raposa',       MAMMAL, ORANGE, FUR,    IGNORE,    SMALL,  CARNIVORE, IGNORE),
    ('Rato',         MAMMAL, GREY,   FUR,    URBAN,     SMALL,  CARNIVORE, YES),
    ('Rinoceronte',  MAMMAL, GREY,   DRY,    GRASSLAND, LARGE,  HERBIVORE, YES),
    ('Tatu',         MAMMAL, IGNORE, SHELL,  IGNORE,    TINY,   HERBIVORE, NO),
    ('Tigre',        MAMMAL, ORANGE, FUR,    GRASSLAND, MEDIUM, CARNIVORE, YES),
    ('Urso',         MAMMAL, BROWN,  FUR,    IGNORE,    LARGE,  CARNIVORE, YES),
    ('Vaca',         MAMMAL, IGNORE, FUR,    GRASSLAND, MEDIUM, HERBIVORE, NO),
    ('Zebra',        MAMMAL, BLACK,  FUR,    GRASSLAND, MEDIUM, HERBIVORE, NO),
    ('Zebra',        MAMMAL, WHITE,  FUR,    GRASSLAND, MEDIUM, HERBIVORE, NO),
)


def load_animals(animals=_animals):
    for animal in animals:
        if Counter(animal)[IGNORE] > 2:
            raise ValueError(
                "can't have more than 2 ignores on the same animal")

    return pd.DataFrame(
        data=list(animals),
        columns=['name', 'type', 'color', 'skin_type',
                 'habitat', 'size', 'diet', 'dangerous'],
    )


load_animals().to_csv(path.join(BASE_DIR, 'animals.csv'))
