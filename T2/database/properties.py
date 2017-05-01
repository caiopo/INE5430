# propreties:
# color
# size
# skin_type
# habitat
# origin

from enum import Enum


class Colors(Enum):
    BLACK = 'Black',
    BLUE = 'Blue',
    BROWN = 'Brown',
    GREEN = 'Green',
    GREY = 'Grey',
    ORANGE = 'Orange',
    PINK = 'Pink',
    PURPLE = 'Purple',
    RED = 'Red',
    WHITE = 'White',
    YELLOW = 'Yellow',
    VARIABLE = 'Variable',


class SkinTypes(Enum):
    DRY = 'Dry',
    FEATHER = 'Feather',
    FUR = 'Fur',
    SCALE = 'Scale',
    SHELL = 'Shell',


class Origins(Enum):
    AFRICA = 'Africa',
    AMERICA = 'America',
    ASIA = 'Asia',
    EUROPE = 'Europe',
    OCEAN = 'Ocean',
    OCEANIA = 'Oceania',
    POLES = 'North/South pole',
    OTHER = 'Other'


class Size(Enum):
    TINY = '< 10 cm',
    SMALL = '10 cm to 1 m',
    MEDIUM = '1 m to 3 m',
    LARGE = '> 3 m',
    VARIABLE = 'Variable',


# TODO
# habitats = (
#     'Forest',
#     'Salt Water',
#     'Fresh Water',
#     'Plain',
#     'Urban',
# )
