from parse import parse_neko

import itertools

with open('48.txt', 'w') as wf:
    for chunks in parse_neko():
        for chunk in chunks:
            if chunk.contains('名詞'):
                crt_chunk = chunk
                wf.write(chunk.get_text())
                while crt_chunk.dst != -1:
                    crt_chunk = chunks[crt_chunk.dst]
                    wf.write(" -> " + crt_chunk.get_text())
                wf.write('\n')
