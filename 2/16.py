
def split(N, filename):
    with open(filename) as rf:
        lines = rf.readlines()
        line_num = len(lines)
        if N > line_num:
            return

        line_num_per_file_small = line_num // N
        line_num_per_file_large = line_num_per_file_small + 1
        large_file_num = line_num % N
        for i in range(N):
            with open('16-' + str(i) + '.txt', 'w') as wf:
                if i < large_file_num:
                    wf.writelines(
                        lines[i * line_num_per_file_large:
                              (i + 1) * line_num_per_file_large])
                else:
                    offset = large_file_num * line_num_per_file_large
                    j = i - large_file_num
                    wf.writelines(
                        lines[offset + j * line_num_per_file_small: offset + (j + 1) * line_num_per_file_small])


N = input()
split(int(N), 'popular-names.txt')
