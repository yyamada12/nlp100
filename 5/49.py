from parse import parse_neko

import itertools


def get_depending_list(chunks, start):
    res = [start]
    crt_chunk = chunks[start]
    while crt_chunk.dst != -1:
        res.append(crt_chunk.dst)
        crt_chunk = chunks[crt_chunk.dst]
    return res


def get_shotest_path(Xs, Ys):
    if Ys[0] in Xs:
        return True, Xs[0:Xs.index(Ys[0])+1]

    res_Ys = []
    for y in Ys:
        if y in Xs:
            res_Xs = Xs[0:Xs.index(y)]
            return False, (res_Xs, res_Ys, y)
        else:
            res_Ys.append(y)


with open('49.txt', 'w') as wf:
    for chunks in parse_neko():
        depending_lists = [get_depending_list(chunks, i)
                           for i, chunk in enumerate(chunks)
                           if chunk.contains('名詞')]

        for i, Xs in enumerate(depending_lists[:-1]):
            for Ys in depending_lists[i+1:]:
                is_connect, paths = get_shotest_path(Xs, Ys)
                if is_connect:
                    first_text = chunks[paths[0]].get_text_sub('X') + ' -> '
                    middle_text = ''.join(
                        chunks[i].get_text() + ' -> ' for i in paths[1:-1])
                    last_text = chunks[paths[-1]].get_text_sub('Y')
                    wf.write(first_text + middle_text + last_text + '\n')
                else:
                    pathX, pathY, common = paths
                    first_block = chunks[pathX[0]].get_text_sub(
                        'X') + ' -> ' + ' -> '.join(chunks[i].get_text() for i in pathX[1:])
                    second_block = chunks[pathY[0]].get_text_sub(
                        'Y') + ' -> ' + ' -> '.join(chunks[i].get_text() for i in pathY[1:])
                    wf.write(first_block + ' | ' + second_block +
                             ' | ' + chunks[common].get_text() + '\n')
