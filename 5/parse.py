from morph import Morph
from chunk import Chunk

from collections import defaultdict


def parse_neko():
    def parse_morph(line):
        tab_splitted = line.split('\t')
        surface = tab_splitted[0]
        comma_splitted = tab_splitted[1].split(',')
        base = comma_splitted[6]
        pos = comma_splitted[0]
        pos1 = comma_splitted[1]
        return Morph(surface, base, pos, pos1)

    def parse_dependency(line, srcs_dict):
        splitted = line.split()
        crt = int(splitted[1])
        dst = int(splitted[2][:-1])
        srcs_dict[dst].append(crt)
        return Chunk([], dst, srcs_dict[crt])

    with open("neko.txt.cabocha") as f:
        chunks = []
        srcs_dict = defaultdict(list)
        for line in f:
            if line.find('*') == 0:
                chunk = parse_dependency(line, srcs_dict)
                chunks.append(chunk)
            elif line.find('EOS') > -1:
                if chunks:
                    yield chunks
                    chunks = []
                    srcs_dict = defaultdict(list)
            else:
                chunk.morphs.append(parse_morph(line))
