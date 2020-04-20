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


def extract_noun_phrase(morphs):
    res = []
    morphs_len = len(morphs)
    for i in range(morphs_len - 2):
        if morphs[i]['pos'] == '名詞' and morphs[i + 1]['surface'] == 'の' and morphs[i + 2]['pos'] == '名詞':
            res.append(morphs[i]['surface'] + morphs[i + 1]
                       ['surface'] + morphs[i + 2]['surface'])
    return res


print(sum([extract_noun_phrase(morphs) for morphs in parse_lines()], []))
