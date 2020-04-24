from morph import Morph


class Chunk:
    def __init__(self, morphs, dst, srcs):
        self.morphs = morphs
        self.dst = dst
        self.srcs = srcs

    def __str__(self):
        return 'morphs: \n' + '\n'.join(['\t' + str(morph) for morph in self.morphs]) \
            + '\ndst: ' + str(self.dst) \
            + '\nsrcs: ' + ','.join([str(src) for src in self.srcs]) + '\n'

    def get_text(self):
        return ''.join([morph.surface for morph in self.morphs if morph.pos != '記号'])

    def get_predicate(self):
        for morph in self.morphs:
            if morph.pos == '動詞':
                return morph.base
        return ''

    def get_particles(self):
        return [morph.base for morph in self.morphs if morph.pos == '助詞']

    def is_noun_with_wo(self):
        morphs_len = len(self.morphs)
        for i in range(morphs_len - 1):
            if self.morphs[i].pos == '名詞' and self.morphs[i].pos1 == 'サ変接続' and self.morphs[i + 1].pos == '助詞' and self.morphs[i + 1].surface == 'を':
                return True
        return False

    def contains(self, pos):
        return any((morph.pos == pos for morph in self.morphs))
