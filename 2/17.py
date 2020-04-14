with open('popular-names.txt') as rf:
    set = {line.split()[0] for line in rf}
with open('17.txt', 'w') as wf:
    for word in sorted(set):
        wf.write(word + '\n')
