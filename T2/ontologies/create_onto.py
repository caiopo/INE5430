from owlready import *
from os.path import realpath
# from types import new_class

onto_path.append(realpath('.'))

onto = Ontology('http://inf.ufsc.br/onto.owl')

# propreties:
# color
# size
# skin_type
# habitat
# origin

color_names = (
    'Black',
    'Blue',
    'Brown',
    'Green',
    'Grey',
    'Orange',
    'Pink',
    'Purple',
    'Red',
    'White',
    'Yellow',
    'Variable',
)

skin_type_names = (
    'Dry',
    'Feather',
    'Fur',
    'Scale',
)

habitat_names = (
    'Forest',
    'SaltWater',
    'FreshWater',
    'Plain',
    'Urban',
)

origin_names = (
    'Africa',
    'America',
    'Asia',
    'Europe',
    'Ocean',
    'Oceania',
    'Poles',
)


class Color(Thing):
    ontology = onto


class SkinType(Thing):
    ontology = onto


class Habitat(Thing):
    ontology = onto


class Origin(Thing):
    ontology = onto


colors = {c: Color(c) for c in color_names}

skin_types = {st: SkinType(st) for st in skin_type_names}

habitats = {h: Habitat(h) for h in habitat_names}

origins = {o: Origin(o) for o in origin_names}


class Animal(Thing):
    ontology = onto


class Fish(Animal):
    pass


class Amphibian(Animal):
    pass


class Reptile(Animal):
    pass


class Bird(Animal):
    pass


class Mammal(Animal):
    pass


class color(FunctionalProperty):
    ontology = onto
    domain = [Animal]
    range = [Color]


class skin_type(FunctionalProperty):
    ontology = onto
    domain = [Animal]
    range = [SkinType]


class habitat(FunctionalProperty):
    ontology = onto
    domain = [Animal]
    range = [Habitat]


class origin(FunctionalProperty):
    ontology = onto
    domain = [Animal]
    range = [Origin]


AllDisjoint(Animal, Color, SkinType, Habitat, Origin)
AllDisjoint(Fish, Amphibian, Reptile, Bird, Mammal)


class Elephant(Mammal):
    equivalent_to = [Mammal &
                     restriction(color, VALUE, colors['Grey']) &
                     restriction(skin_type, VALUE, skin_types['Dry']) &
                     restriction(habitat, VALUE, habitats['Plain']) &
                     restriction(origin, VALUE, origins['Africa'])]


onto.save()

x = onto.Mammal(color=colors['Grey'])

print(x.__class__)

onto.sync_reasoner()

print(x.__class__)

print(vars(onto.Animal))



