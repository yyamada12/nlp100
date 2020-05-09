import numpy as np
import tensorflow as tf

train_X = np.load('train_X.npy')
train_y = np.load('train_y.npy')

W = tf.random.truncated_normal([300, 4])
x1 = tf.convert_to_tensor(train_X[0].reshape(1, 300), np.float32)
X1_4 = tf.convert_to_tensor(train_X[:4], np.float32)

y1 = tf.nn.softmax(tf.matmul(x1, W))
Y = tf.nn.softmax(tf.matmul(X1_4, W))

print("y1:\n", y1)
print("Y:\n", Y)
