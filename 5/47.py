from parse import parse_neko

import itertools

with open('47.txt', 'w') as wf:
    for chunks in parse_neko():
        for chunk in chunks:
            if chunk.contains('動詞') and chunk.srcs != []:
                predicate = ''
                srcs = []
                for src in chunk.srcs:
                    if chunks[src].is_noun_with_wo():
                        predicate = chunks[src].get_text() + \
                            chunk.get_predicate()
                        srcs = chunk.srcs.copy()
                        srcs.remove(src)
                        break
                if predicate:
                    particles_text = ' '.join(itertools.chain.from_iterable(
                        chunks[src].get_particles() for src in srcs))
                    depending_text = ' '.join(
                        chunks[src].get_text() for src in srcs if chunks[src].contains('助詞'))
                    if particles_text:
                        wf.write(predicate +
                                 '\t' + particles_text + '\t' + depending_text + '\n')
