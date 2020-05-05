from gensim.models import KeyedVectors
import numpy as np
from scipy.stats import spearmanr
from tqdm import tqdm


model = KeyedVectors.load_word2vec_format(
    './GoogleNews-vectors-negative300.bin', binary=True)

human_score = []
w2v_score = []

with open('./wordsim353/combined.tab') as f:
    f.readline()  # discard header
    for line in tqdm(f):
        elements = line.split()
        w2v_score.append(model.similarity(elements[0], elements[1]))
        human_score.append(elements[2])

human_rank = np.argsort(np.argsort(human_score))
w2v_rank = np.argsort(np.argsort(w2v_score))

correlation, _ = spearmanr(human_rank, w2v_rank)
print(correlation)
