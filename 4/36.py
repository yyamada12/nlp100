import csv
import collections
import matplotlib.pyplot as plt
from matplotlib import rcParams
rcParams['font.family'] = 'sans-serif'
rcParams['font.sans-serif'] = ['Hiragino Maru Gothic Pro', 'Yu Gothic', 'Meirio',
                               'Takao', 'IPAexGothic', 'IPAPGothic', 'VL PGothic', 'Noto Sans CJK JP']


def parse_mecab(line):
    res = {}
    if line.find('EOS') > -1:
        return res
    tab_splitted = line.split('\t')
    res['surface'] = tab_splitted[0]
    comma_splitted = tab_splitted[1].split(',')
    res['base'] = comma_splitted[6]
    res['pos'] = comma_splitted[0]
    res['pos1'] = comma_splitted[1]
    return res


def parse_lines():
    with open("neko.txt.mecab") as f:
        res = []
        for line in f:
            morph = parse_mecab(line)
            if morph:
                res.append(morph)
            else:
                yield res
                res = []


def extract_surface(morphs):
    return [morph['surface'] for morph in morphs]


TF = collections.Counter(sum([extract_surface(morphs)
                              for morphs in parse_lines()], []))

words = []
freqs = []
for word, freq in TF.most_common(10):
    words.append(word)
    freqs.append(freq)

plt.bar(range(10), freqs, tick_label=words)
plt.savefig('36.png')
