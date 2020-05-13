import numpy as np
import tensorflow as tf
from tensorflow import keras

train_X = np.load('train_X.npy')
train_y = np.load('train_y.npy')
valid_X = np.load('valid_X.npy')
valid_y = np.load('valid_y.npy')


model = keras.Sequential([
    keras.layers.Dense(4, use_bias=False)
])
model.compile(optimizer='sgd',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(
                  from_logits=True),
              metrics=['accuracy'])


model.load_weights('./73.checkpoint')
loss, acc = model.evaluate(train_X,  train_y, verbose=2)
print('train: ' + str(acc))
loss, acc = model.evaluate(valid_X,  valid_y, verbose=2)
print('valid: ' + str(acc))
