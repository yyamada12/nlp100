from gensim.models import KeyedVectors
import matplotlib.pyplot as plt
from sklearn.manifold import TSNE

model = KeyedVectors.load_word2vec_format(
    './GoogleNews-vectors-negative300.bin', binary=True)

countries_set = set()
category = ''
with open('questions-words.txt') as rf:
    for line in rf:
        if line.startswith(':'):
            category = line[2:].rstrip()
            continue
        if category in ['capital-common-countries', 'capital-world']:
            words = line.split()
            countries_set.add(words[1])
            countries_set.add(words[3])
        elif category in ['currency', 'gram6-nationality-adjective']:
            words = line.split()
            countries_set.add(words[0])
            countries_set.add(words[2])

countries_list = list(countries_set)
X = [model[country] for country in countries_list]
X_reduced = TSNE(n_components=2, random_state=0).fit_transform(X)

plt.figure(figsize=(16, 16))
plt.scatter(X_reduced[:, 0], X_reduced[:, 1])
for (x, y), name in zip(X_reduced, countries_list):
    plt.annotate(name, (x, y))
plt.savefig('69.png')
