with open('popular-names.txt') as rf:
    lines = rf.readlines()
sorted_lines = sorted(lines,
                      key=(lambda line: int(line.split()[2])), reverse=True)
with open('18.txt', 'w') as wf:
    wf.writelines(sorted_lines)
