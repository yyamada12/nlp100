from morph import Morph


def parse_lines():
    def parse_morph(line):
        tab_splitted = line.split('\t')
        surface = tab_splitted[0]
        comma_splitted = tab_splitted[1].split(',')
        base = comma_splitted[6]
        pos = comma_splitted[0]
        pos1 = comma_splitted[1]
        return Morph(surface, base, pos, pos1)

    with open("neko.txt.cabocha") as f:
        res = []
        for line in f:
            if line.find('*') == 0:
                continue
            if line.find('EOS') > -1:
                yield res
                res = []
                continue
            res.append(parse_morph(line))


for morph in [morphs for morphs in parse_lines() if morphs][2]:
    print(morph)
