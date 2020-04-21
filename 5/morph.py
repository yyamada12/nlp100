class Morph:
    def __init__(self, surface, base, pos, pos1):
        self.surface = surface
        self.base = base
        self.pos = pos
        self.pos1 = pos1

    def __str__(self):
        return 'surface: ' + self.surface \
            + '\tbase: ' + self.base \
            + '\tpos: ' + self.pos \
            + '\tpos1: ' + self.pos1
