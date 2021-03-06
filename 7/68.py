from gensim.models import KeyedVectors
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage, fcluster

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

Z = linkage(X, method="ward", metric="euclidean")
plt.figure(figsize=(16, 9))
dendrogram(Z, labels=countries_list, leaf_font_size=6)
plt.savefig('68.png')
