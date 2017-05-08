from animals import *


YES = 'yes'
NO = 'no'
UNKNOWN = 'unknown'


# columns = (
#     'type', 'color', 'skin_type', 'habitat', 'size', 'diet', 'dangerous'
# )


def _ask_type(t):
    return 'O animal é um {}?'.format(t.lower())


def _ask_color(c):
    return 'Todos os animais desta espécie possuem a cor {}?'.format(c.lower())


def _ask_skin_type(st):
    return 'O tipo de pele do animal é "{}"?'.format(st)


def _ask_habitat(h):
    return 'O habitat do animal é "{}"?'.format(h)


def _ask_size(s):
    size = {
        TINY: 'menos de 10 centímetros',
        SMALL: 'entre 10 centímetros e 1 metro',
        MEDIUM: 'entre 1 e 2 metros',
        LARGE: 'mais que 2 metros',
    }[s]

    return 'O animal tem {}?'.format(size)


def _ask_diet(d):
    return 'O animal é {}?'.format(d.lower())


# def _ask_dangerous(d):
#     if d:
#         return 'O animal é perigoso para humanos?'
#     return 'O animal NÃO é perigoso para humanos?'


questions = {
    'type': _ask_type,
    'color': _ask_color,
    'skin_type': _ask_skin_type,
    'habitat': _ask_habitat,
    'size': _ask_size,
    'diet': _ask_diet,
    # 'dangerous': _ask_dangerous,
}


def _input(invert=False):
    inp = input()

    b = {
        'y': YES,
        'n': NO,
    }.get(inp, UNKNOWN)

    if invert:
        if b == YES:
            b = NO
        elif b == NO:
            b = YES

    print(b)

    return b


def ask_user(prop, category):
    try:
        print(questions[prop](category))

        return _input()

    except KeyError:
        print('O animal é perigoso para humanos?')

        if category:
            return _input()
        return _input(invert=True)
