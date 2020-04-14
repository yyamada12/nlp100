with open('col1.txt') as col1:
    with open('col2.txt') as col2:
        with open('13.txt', 'w') as wf:
            for line1, line2 in zip(col1, col2):
                wf.write(line1.rstrip('\n') + '\t' + line2)
