from classifier import Classifier
from questions import ask_user, ask_animal_is
from animals import load_animals, columns


class Controller:
    def run_classifier(self):
        self.classifier = Classifier(load_animals(), ask_user)

        print('Responda com "y" para Sim e "n" para Não\nQualquer outra '
              'resposta será interpretada como "não sei/talvez"\n')

        return self.classifier.discover_animals()

    def run_names(self, animals):
        names = sorted(animals)

        for name in names:
            if ask_animal_is(name):
                return name

    def finish(self, animal):
        animal = list(animal)

        if len(animal) == 0:
            print('Nenhum animal encontrado.')
            return

        animal = animal[0]

        if animal is None:
            print('Nenhum animal encontrado.')
            return

        print('O animal é {}!'.format(animal))
        print('Fim')

    def run(self):
        animals = list(self.run_classifier().name.unique())

        if len(animals) > 1:
            animals = [self.run_names(animals)]

        self.finish(animals)

if __name__ == '__main__':
    controller = Controller()

    controller.run()
