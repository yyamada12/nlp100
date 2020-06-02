import collections
import datetime
import numpy as np
import pandas as pd
import subprocess
import tensorflow as tf
from tensorflow import keras


subprocess.run(["rm", "-rf", "./logs/"])


def count_words(title_list):
    c = collections.Counter(
        word for title in title_list for word in title.split())
    return {word: i + 1 for i, (word, cnt) in enumerate(c.most_common()) if cnt > 1}


def label_encoder(title, word_dict):
    return [word_dict.get(word, 0) for word in title.split()]


train_df = pd.read_table('./train.txt')
valid_df = pd.read_table('./valid.txt')
word_dict = count_words(train_df['TITLE'])
num_words = len(word_dict) + 1  # word not in dict is labeled as 0

# label encode and padding with 0
train_X = keras.preprocessing.sequence.pad_sequences(
    train_df['TITLE'].map(lambda x: label_encoder(x, word_dict)))
valid_X = keras.preprocessing.sequence.pad_sequences(
    valid_df['TITLE'].map(lambda x: label_encoder(x, word_dict)), maxlen=(train_X.shape[1]))

train_y = train_df['CATEGORY'].map({'b': 0, 't': 1, 'e': 2, 'm': 3}).values
valid_y = valid_df['CATEGORY'].map({'b': 0, 't': 1, 'e': 2, 'm': 3}).values

model = keras.Sequential([
    keras.layers.Embedding(num_words, 300, mask_zero=True),
    keras.layers.Conv1D(50, 3, activation="relu"),
    keras.layers.MaxPooling1D(train_X.shape[1]-2),
    keras.layers.Dense(4, activation='tanh')
])
model.compile(optimizer='sgd',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(
                  from_logits=True),
              metrics=['accuracy'])

log_dir = "logs/fit/" + datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
tensorboard_callback = tf.keras.callbacks.TensorBoard(
    log_dir=log_dir, histogram_freq=1)

model.fit(train_X, train_y, epochs=10, validation_data=(valid_X, valid_y),
          callbacks=[tensorboard_callback])
