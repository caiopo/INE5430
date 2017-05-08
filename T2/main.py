from classifier import Classifier
from questions import ask_user
from animals import load_animals


class Controller:
    def run_classifier(self):
        c = Classifier(load_animals(), ask_user)

        print('Responda com "y" para Sim e "n" para Não\nQualquer outra '
              'resposta será interpretada como "não sei/talvez"\n')

        return c.discover_animals()

    def run_names(self, animals):
        names = animals.name.unique()

        print(names)

    def finish(self, animal):
        pass

    def wrong(self):
        pass

    def run(self):
        animals = self.run_classifier()

        print(animals)

        if len(animals) > 1:
            animals = self.run_names(animals)

        print(animals)


if __name__ == '__main__':
    controller = Controller()

    controller.run()
