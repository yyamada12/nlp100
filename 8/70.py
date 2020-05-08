from gensim.models import KeyedVectors
import numpy as np
import pandas as pd

model = KeyedVectors.load_word2vec_format(
    './GoogleNews-vectors-negative300.bin', binary=True)


train_df = pd.read_table('train.txt')
valid_df = pd.read_table('valid.txt')
test_df = pd.read_table('test.txt')


def avg_emb(sentence, model):
    res = np.mean([model[word]
                   for word in sentence.split() if word in model.vocab], axis=0)
    if type(res) is np.ndarray:
        return res
    else:
        # no words in model
        print("no words in w2v: " + sentence)
        return np.zeros((300,), dtype="float32")


for data in ['train', 'valid', 'test']:
    df = pd.read_table(data + '.txt')
    X = [avg_emb(title, model).tolist() for title in df['TITLE']]
    y = df['CATEGORY'].map({'b': 0, 't': 1, 'e': 2, 'm': 3}).values
    np.save(data + '_X.npy', X)
    np.save(data + '_y.npy', y)
