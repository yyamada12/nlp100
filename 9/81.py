import collections
import numpy as np
import pandas as pd
import tensorflow as tf


def count_words(title_list):
    c = collections.Counter(
        word for title in title_list for word in title.split())
    return {word: i + 1 for i, (word, cnt) in enumerate(c.most_common()) if cnt > 1}


def label_encoder(title, word_dict):
    return [word_dict.get(word, 0) for word in title.split()]


train_df = pd.read_table('./train.txt')
word_dict = count_words(train_df['TITLE'])

print(label_encoder(train_df['TITLE'][0], word_dict))

num_words = len(word_dict) + 1  # word not in dict is labeled as 0

title0 = label_encoder(train_df['TITLE'][0], word_dict)
X = np.identity(num_words)[title0]

Wemb = np.random.randn(num_words, 300)

Whx = np.random.randn(300, 50)
Whh = np.random.randn(50, 50)
bh = np.random.randn(1, 50)

Wyh = np.random.randn(50, 4)
by = np.random.randn(1, 4)

h = np.zeros((1, 50))

for x in X:
    h = tf.nn.relu((x.reshape(1, num_words) @ Wemb) @ Whx + h @ Whh + bh)
y = tf.nn.softmax(h @ Wyh + by)
print(y)
