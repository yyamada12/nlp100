import joblib
import pandas as pd
from sklearn.metrics import confusion_matrix

train_X = pd.read_table('train.feature.txt')
train_y = pd.read_table('train.label.txt')

valid_X = pd.read_table('valid.feature.txt')
valid_y = pd.read_table('valid.label.txt')

lr = joblib.load('52.Joblib')
predicts_train = lr.predict(train_X)
predicts_valid = lr.predict(valid_X)

labels = ['b', 'e', 'm', 't']
print('train:')
print(labels)
print(confusion_matrix(train_y, predicts_train, labels=labels))

print('valid:')
print(labels)
print(confusion_matrix(valid_y, predicts_valid, labels=labels))
