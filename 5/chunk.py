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

    def contains(self, pos):
        return any((morph.pos == pos for morph in self.morphs))
