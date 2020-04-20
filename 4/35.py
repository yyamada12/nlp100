import csv
import collections


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
print(TF.most_common())
