import datetime
import numpy as np
import subprocess
import tensorflow as tf
from tensorflow import keras
import time

# remove old log files
subprocess.run(["rm", "-rf", "./logs/"])

# load data
train_X = np.load('train_X.npy')
train_y = np.load('train_y.npy')
valid_X = np.load('valid_X.npy')
valid_y = np.load('valid_y.npy')

# create model


def fit_model(batch_size, tensorboard_callback, cp_callback):
    model = keras.Sequential([
        keras.layers.Dense(4, use_bias=False)
    ])
    model.compile(optimizer='sgd',
                  loss=tf.keras.losses.SparseCategoricalCrossentropy(
                      from_logits=True),
                  metrics=['accuracy'])
    model.fit(train_X, train_y, batch_size=batch_size, epochs=1,
              validation_data=(valid_X, valid_y),
              callbacks=[tensorboard_callback, cp_callback])


# log settings
log_dir = "logs/fit/" + datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
tensorboard_callback = tf.keras.callbacks.TensorBoard(
    log_dir=log_dir, histogram_freq=1)

# checkpoint settings
checkpoint_path = "checkpoints/cp-{epoch:04d}.ckpt"
cp_callback = tf.keras.callbacks.ModelCheckpoint(checkpoint_path,
                                                 verbose=1)

for i in range(4):
    start = time.time()
    fit_model(2**i, tensorboard_callback, cp_callback)
    end = time.time()
    print("batch_size: " + str(2**i))
    print("elapsed time: " + str(end-start))

# watch progress with `tensorboard --logdir logs/fit`
