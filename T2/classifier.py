from animals import load_animals, IGNORE
from statistics import mean


class Classifier:
    def __init__(self, df, ask):
        """
        df: pandas.DataFrame containing the data, first column is considered
            identification and will not be used in the algorithm

        ask: callback that receives a property and a category and returns a
            boolean indicating if the target element is part of this category
        """

        self.df = df.copy()
        self.ask = ask
        self.properties = list(df.columns[1:])
        self.info = {}

    def largest_group(self):
        global_groups = []

        for prop in self.properties:
            groups = self.df.groupby(prop)

            prop_max = max(groups.groups.items(),
                           key=lambda d: len(d[1]) if d[0] != IGNORE else 0)

            global_groups.append((prop,) + prop_max)

        return max(global_groups, key=lambda item: len(item[2]))

    def discover_animals(self):
        while self._can_continue():

            prop, category, indexes = self.largest_group()

            if self.ask(prop, category):
                self.properties.remove(prop)
                self.df = self.df.loc[indexes]
                self.info[prop] = category
            else:
                self.df.drop(indexes, inplace=True)

        return self.df

    def _can_continue(self):
        values = self.df.drop('name', axis=1)

        return len(values.drop_duplicates()) != 1