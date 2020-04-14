with open('popular-names.txt') as rf:
    with open('col1.txt', 'w') as col1:
        with open('col2.txt', 'w') as col2:
            for line in rf:
                splitted = line.split()
                col1.write(splitted[0] + '\n')
                col2.write(splitted[1] + '\n')
