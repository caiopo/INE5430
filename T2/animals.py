import pandas as pd

from os import path
from properties import Colors, SkinTypes, Origins, Size
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
DRY = 'Seca'
FEATHER = 'Pena'
FUR = 'Pêlo'
SCALE = 'Escama'
SHELL = 'Casco'
WET = 'Úmida'

# Habitat
DESERT = 'Deserto'
FRESHWATER = 'Água Doce'
GRASSLAND = 'Grassland'
MOUNTAINS = 'Montanha'
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
OMNIVORE = 'Omnívoro'

IGNORE = 'ignore'
YES = 'sim'
NO = 'não'

# alpaca
# anta
# antilope
# burro
# camelo
# canguru
# capivara
# cavalo marinho
# cervo
# chipanze
# coelho
# corvo
# flamingo
# foca
# gaivota
# galinha
# guaxinim
# hiena
# hipopotamo
# humanos
# jaguatirica
# leao marinho
# lemure
# lontra
# morcego
# mula
# onca
# ornitorrinco
# ovelha
# porco
# porco espinho
# quati
# rato
# rinoceronte
# tamanduá
# tatu
# tigre
# unicornio
# urso
# zebra

_animals = (
    ('Peixinho-dourado', FISH, ORANGE, SCALE, FRESHWATER, TINY,   OMNIVORE),
    ('Orca',             FISH, BLACK,  WET,   OCEAN,  LARGE,  CARNIVORE),
    ('Salmão',           FISH, GREY,   SCALE, OCEAN,  SMALL,  OMNIVORE),
    ('Tubarão',          FISH, GREY,   WET,   OCEAN,  LARGE,  CARNIVORE),
    ('Boto',             FISH, PINK,   WET,   OCEAN,  MEDIUM, CARNIVORE),
    ('Tainha',           FISH, GREY,   WET,   OCEAN,  SMALL,  OMNIVORE),
    ('Golfinho',         FISH, GREY,   WET,   OCEAN,  LARGE,  CARNIVORE),

    # revisar anfíbios
    ('Sapo',       AMPHIBIAN, GREEN, WET, IGNORE, SMALL, CARNIVORE),
    ('Pereca',     AMPHIBIAN, GREEN, WET, IGNORE, SMALL, CARNIVORE),
    ('Rã',         AMPHIBIAN, GREEN, WET, IGNORE, SMALL, CARNIVORE),
    ('Rã',         AMPHIBIAN, BROWN, WET, IGNORE, SMALL, CARNIVORE),
    ('Salamandra', AMPHIBIAN, GREEN, WET, IGNORE, SMALL, CARNIVORE),

    ('Crocodilo', REPTILE, GREEN,  DRY,   IGNORE, LARGE, CARNIVORE),
    ('Jacaré',    REPTILE, GREEN,  DRY,   IGNORE, LARGE, CARNIVORE),
    ('Tartaruga', REPTILE, BROWN,  SHELL, IGNORE, SMALL, OMNIVORE),
    ('Lagarto',   REPTILE, IGNORE, SCALE, IGNORE, SMALL, OMNIVORE),
    ('Jibóia',    REPTILE, BROWN,  DRY,   IGNORE, LARGE, CARNIVORE),
    ('Dragão',    REPTILE, IGNORE, SCALE, IGNORE, LARGE, CARNIVORE),

    ('Pato',     BIRD, IGNORE, FEATHER, IGNORE,  SMALL,  OMNIVORE),
    ('Águia',    BIRD, BROWN,  FEATHER, AMERICA, MEDIUM, CARNIVORE),
    ('Falcão',   BIRD, BROWN,  FEATHER, IGNORE,  SMALL,  CARNIVORE),
    ('Cisne',    BIRD, WHITE,  FEATHER, AMERICA, IGNORE, OMNIVORE),
    ('Papagaio', BIRD, GREEN,  FEATHER, IGNORE, IGNORE, HERBIVORE),
    ('Pinguim',  BIRD, BLACK,  FEATHER, IGNORE, IGNORE, OMNIVORE),
    ('Coruja',   BIRD, WHITE,  FEATHER, IGNORE, IGNORE, OMNIVORE),
    ('Gaviao',   BIRD, WHITE,  FEATHER, IGNORE, IGNORE, OMNIVORE),
    ('Picapau',  BIRD, WHITE,  FEATHER, IGNORE, IGNORE, OMNIVORE),
    ('Avestruz', BIRD, WHITE,  FEATHER, IGNORE, IGNORE, OMNIVORE),
    ('Ema',      BIRD, WHITE,  FEATHER, IGNORE, IGNORE, OMNIVORE),

    ('Macaco',      MAMMAL, BROWN,  FUR, OCEAN,  LARGE,  OMNIVORE),
    ('Baleia',      MAMMAL, GREY,   WET, OCEAN,  LARGE,  CARNIVORE),
    ('Gato',        MAMMAL, IGNORE, FUR, IGNORE, SMALL,  CARNIVORE),
    ('Vaca',        MAMMAL, IGNORE, FUR, IGNORE, MEDIUM, CARNIVORE),
    ('Cachorro',    MAMMAL, IGNORE, FUR, IGNORE, SMALL,  CARNIVORE),
    ('Elefante',    MAMMAL, GREY,   DRY, AFRICA, LARGE,  HERBIVORE),
    ('Girafa',      MAMMAL, BROWN,  FUR, AFRICA, LARGE,  HERBIVORE),
    ('Cavalo',      MAMMAL, IGNORE, FUR, IGNORE, MEDIUM, HERBIVORE),
    ('Leão',        MAMMAL, YELLOW, FUR, AFRICA, MEDIUM, CARNIVORE),
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
