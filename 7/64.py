from gensim.models import KeyedVectors
from tqdm import tqdm

model = KeyedVectors.load_word2vec_format(
    './GoogleNews-vectors-negative300.bin', binary=True)

with open('questions-words.txt') as rf, open('questions-words-predict.txt', 'w') as wf:
    for line in tqdm(rf):
        if line.startswith(':'):
            wf.write(line)
            continue
        words = line.split()
        word, similarity = model.most_similar(
            positive=[words[1], words[2]],  negative=[words[0]], topn=1)[0]
        wf.write(' '.join(words + [word, str(similarity)]) + '\n')
