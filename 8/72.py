import numpy as np
import tensorflow as tf

train_X = np.load('train_X.npy')
train_y = np.load('train_y.npy')

W = tf.Variable(tf.random.truncated_normal([300, 4], seed=1))
x1 = train_X[0].reshape(1, 300)
X1_4 = train_X[:4]

print("x1:")
with tf.GradientTape() as t:
    loss = tf.keras.losses.sparse_categorical_crossentropy(
        train_y[0], x1 @ W, from_logits=True)
print(loss)
print(t.gradient(loss, W))
print()

print("X1_4:")
with tf.GradientTape() as t:
    loss = tf.keras.backend.mean(tf.keras.losses.sparse_categorical_crossentropy(
        train_y[:4], X1_4 @ W, from_logits=True))
print(loss)
print(t.gradient(loss, W))
