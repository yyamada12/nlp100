import pandas as pd
import collections


def count_words(title_list):
    c = collections.Counter(
        word for title in title_list for word in title.split())
    return {word: i + 1 for i, (word, cnt) in enumerate(c.most_common()) if cnt > 1}


def label_encoder(title, word_dict):
    return [word_dict.get(word, 0) for word in title.split()]


train_df = pd.read_table('./train.txt')
word_dict = count_words(train_df['TITLE'])

print(label_encoder(train_df['TITLE'][0], word_dict))
