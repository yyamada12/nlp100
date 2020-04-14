N = input()
with open('popular-names.txt') as rf:
    with open('15-' + N + 'lines.txt', 'w') as wf:
        lines = rf.readlines()
        N = min(int(N), len(lines))
        wf.writelines(lines[-N:])
