from parse import parse_neko

for i, chunks in enumerate(parse_neko()):
    if i == 7:
        for chunk in chunks:
            print(chunk)
        break
