from parse import parse_neko

for i, chunks in enumerate(parse_neko()):
    if i == 7:
        for chunk in chunks:
            if chunk.contains('名詞') and chunk.dst != -1 and chunks[chunk.dst].contains('動詞'):
                print(chunk.get_text() + '\t' + chunks[chunk.dst].get_text())
