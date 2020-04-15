import collections

with open('popular-names.txt') as rf:
    collection = collections.Counter(line.split()[0] for line in rf)

with open('19.txt', 'w') as wf:
    for word, _ in collection.most_common():
        wf.write(word + '\n')
