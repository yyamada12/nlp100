N = input()
with open('popular-names.txt') as rf:
    with open('14-' + N + 'lines.txt', 'w') as wf:
        N = int(N)
        i = 0
        for line in rf:
            if i < N:
                wf.write(line)
            i += 1
