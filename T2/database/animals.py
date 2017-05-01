from properties import Colors, SkinTypes, Origins, Size

# ideia de algoritmo:
# 1. carrega um dataframe com todos os dados
# 2. procura o maior grupo de linhas (groupby) em qualquer coluna
# 3. pergunta se o animal pensado pertence a esse grupo
# 4. se sim: descarta tudo que não faz parte do grupo
# 5. se não: descarta tudo que faz parte do grupo
# 6. se não souber: procura o segundo maior grupo e continua do passo 3
# 7. repete do passo 2 até só ter um animal
# -> cuidado com os ignores

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

animals = []


def insert(animal_name, type_, color, skin_type, origin, size):
    animals.append({
        'animal_name': animal_name,
        'type': type_,
        'color': color,
        'skin_type': skin_type,
        'origin': origin,
        'size': size,
    })


insert('Goldfish', FISH, ORANGE, SCALE, IGNORE, TINY)
insert('Orca', FISH, BLACK, WET, OCEAN, LARGE)
insert('Salmon', FISH, GREY, SCALE, OCEAN, SMALL)

insert('Frog', AMPHIBIAN, GREEN, WET, IGNORE, SMALL)

insert('Snake', REPTILE, IGNORE, SCALE, IGNORE, IGNORE)  # revisar
insert('Turtle', REPTILE, BROWN, SHELL, IGNORE, SMALL)

insert('Duck', BIRD, IGNORE, FEATHER, IGNORE, SMALL)
insert('Eagle', BIRD, BROWN, FEATHER, AMERICA, MEDIUM)

insert('Blue Whale', MAMMAL, GREY, WET, OCEAN, LARGE)
insert('Cat', MAMMAL, IGNORE, FUR, IGNORE, SMALL)
insert('Cow', MAMMAL, IGNORE, FUR, IGNORE, MEDIUM)
insert('Dog', MAMMAL, IGNORE, FUR, IGNORE, SMALL)
insert('Elephant', MAMMAL, GREY, DRY, AFRICA, LARGE)
insert('Giraffe', MAMMAL, BROWN, FUR, AFRICA, LARGE)
insert('Horse', MAMMAL, IGNORE, FUR, IGNORE, MEDIUM)
insert('Lion', MAMMAL, YELLOW, FUR, AFRICA, MEDIUM)


if __name__ == '__main__':
    import pandas as pd

    columns = ['animal_name', 'type', 'color', 'skin_type', 'origin', 'size']

    df = pd.DataFrame(data=animals, columns=columns)

    df.to_csv('animals.csv')

    print(df.sort_values('type'))

    import sys

    print(sys.getsizeof(df))

    print(df.memory_usage(deep=True))
