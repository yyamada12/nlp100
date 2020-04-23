from parse import parse_neko

import itertools

with open('46.txt', 'w') as wf:
    for chunks in parse_neko():
        for chunk in chunks:
            if chunk.contains('動詞') and chunk.srcs != []:
                particles_text = ' '.join(itertools.chain.from_iterable(
                    chunks[src].get_particles() for src in chunk.srcs))
                depending_text = ' '.join(
                    chunks[src].get_text() for src in chunk.srcs if chunks[src].contains('助詞'))
                if particles_text:
                    wf.write(chunk.get_predicate() +
                             '\t' + particles_text + '\t' + depending_text + '\n')
