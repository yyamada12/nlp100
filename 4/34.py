import csv


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


def extract_noun_connection(morphs):
    res = []
    nouns = []
    for morph in morphs:
        if morph['pos'] == '名詞':
            nouns.append(morph['surface'])
        else:
            if len(nouns) > 1:
                res.append(''.join(nouns))
            nouns = []
    if len(nouns) > 1:
        res.append(''.join(nouns))
    return res


print(sum([extract_noun_connection(morphs) for morphs in parse_lines()], []))
