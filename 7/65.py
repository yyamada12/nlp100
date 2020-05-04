with open('questions-words-predict.txt') as f:
    syntactic = False
    semantic_list = []
    syntactic_list = []
    for line in f:
        if line.startswith(':'):
            syntactic = 'gram' in line
            continue
        words = line.split()
        if not syntactic:
            semantic_list.append(words[3] == words[4])
        else:
            syntactic_list.append(words[3] == words[4])

print('Accuracy for semantic analogy: ')
print(semantic_list.count(True) / len(semantic_list))
print('Accuracy for syntactic analogy: ')
print(syntactic_list.count(True) / len(syntactic_list))
