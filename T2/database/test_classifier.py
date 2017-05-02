import unittest
from animals import load_animals
from classifier import Classifier, make_ask


class ClassifierTest(unittest.TestCase):

    def setUp(self):
        self.df = load_animals()

    def test_discover(self):
        for animal in self.df.to_dict(orient='records'):
            ask = make_ask(animal)

            classifier = Classifier(self.df, ask)

            result = classifier.discover_animals()

            self.assertIn(animal['name'], list(result.name))
