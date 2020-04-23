from parse import parse_neko

import itertools

with open('45.txt', 'w') as wf:
    for chunks in parse_neko():
        for chunk in chunks:
            if chunk.contains('動詞') and chunk.srcs != []:
                particles_text = ' '.join(itertools.chain.from_iterable(
                    (chunks[src].get_particles()) for src in chunk.srcs))
                if particles_text:
                    wf.write(chunk.get_predicate() +
                             '\t' + particles_text + '\n')
