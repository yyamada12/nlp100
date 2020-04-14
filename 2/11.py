with open('popular-names.txt') as rf:
    with open('11.txt', 'w') as wf:
        for line in rf:
            wf.write(line.replace('\t', ' '))
