from gensim.models import KeyedVectors
from sklearn.cluster import KMeans

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
kmeans = KMeans(n_clusters=5, random_state=0, n_jobs=-1).fit(X)
for country, cluster in zip(countries_list, kmeans.labels_):
    print(country, cluster)
