import unittest

from statistics import mean

from animals import load_animals, IGNORE
from classifier import Classifier
from questions import YES, NO, UNKNOWN


def make_ask(chosen):
    count = 0

    def ask(prop, category):
        nonlocal count
        count += 1

        if category == IGNORE:
            raise ValueError(prop)

        if chosen[prop] == category:
            return YES
        return NO

    setattr(ask, 'count', lambda: count)

    return ask


class ClassifierTest(unittest.TestCase):

    def setUp(self):
        self.df = load_animals()

    def test_discover(self):
        count = []

        for animal in self.df.to_dict(orient='records'):
            ask = make_ask(animal)

            classifier = Classifier(self.df, ask)

            result = classifier.discover_animals()

            # print(animal['name'], list(result.name), classifier.info)

            self.assertIn(animal['name'], list(result.name))

            count.append(ask.count())

        print(mean(count))

    def test_load_fail(self):
        with self.assertRaises(ValueError):
            load_animals(
                [('Any', IGNORE, IGNORE, IGNORE, 'x', 'y', 'z')],
            )


if __name__ == '__main__':
    unittest.main()
