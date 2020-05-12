import numpy as np
import tensorflow as tf
from tensorflow import keras

train_X = np.load('train_X.npy')
train_y = np.load('train_y.npy')

model = keras.Sequential([
    keras.layers.Dense(4, use_bias=False)
])
model.compile(optimizer='sgd',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(
                  from_logits=True),
              metrics=['accuracy'])


model.fit(train_X, train_y, epochs=100)
print(model.layers[0].weights[0])

model.save_weights('./73.checkpoint')
