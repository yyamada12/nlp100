from parse import parse_neko

import pydot

for i, chunks in enumerate(parse_neko()):
    if i == 7:
        edges = []
        for chunk in chunks:
            if chunk.dst != -1:
                edges.append((chunk.get_text(), chunks[chunk.dst].get_text()))
        g = pydot.graph_from_edges(edges)
        g.write_jpeg('44.jpg', prog='dot')
