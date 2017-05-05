import unittest
from animals import load_animals, IGNORE
from classifier import Classifier


def make_ask(chosen):
    count = 0

    def ask(prop, category):
        nonlocal count
        count += 1
        return chosen[prop] == category

    setattr(ask, 'count', lambda: count)

    return ask


class ClassifierTest(unittest.TestCase):

    def setUp(self):
        self.df = load_animals()

    def test_discover(self):
        for animal in self.df.to_dict(orient='records'):
            ask = make_ask(animal)

            classifier = Classifier(self.df, ask)

            result = classifier.discover_animals()

            self.assertIn(animal['name'], list(result.name))

    def test_load_fail(self):
        with self.assertRaises(ValueError):
            load_animals(
                [('Any', IGNORE, IGNORE, IGNORE, 'x', 'y', 'z')],
            )


if __name__ == '__main__':
    unittest.main()
