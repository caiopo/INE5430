from random import randint
from collections import defaultdict


def plot(names, values, feature, filename):
    import seaborn as sns
    import matplotlib.pyplot as plt

    f, ax = plt.subplots(figsize=(20, 5))

    sns.set_style("whitegrid")
    ax = sns.barplot(x=names, y=values, palette='rainbow')
    ax.set(xlabel='', ylabel='')

    sns.despine(bottom=True)
    plt.setp(f.axes)
    plt.tight_layout(h_pad=3)

    ax.get_figure().savefig(filename)


def rand():
    return randint(0, 10)


def iteration():
    return sum(rand() for _ in range(10))


results = defaultdict(int)

for i in range(10000):
    it = iteration()

    results[it] += 1


names = [x[0] for x in results.items()]
values = [x[1] for x in results.items()]

plot(names, values, 'a', 'teste.png')

print(sorted(results.items()))
