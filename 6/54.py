import joblib
import pandas as pd
from sklearn.metrics import accuracy_score

train_X = pd.read_table('train.feature.txt')
train_y = pd.read_table('train.label.txt')

valid_X = pd.read_table('valid.feature.txt')
valid_y = pd.read_table('valid.label.txt')

lr = joblib.load('52.Joblib')
predicts_train = lr.predict(train_X)
predicts_valid = lr.predict(valid_X)

print('train:')
print(accuracy_score(train_y, predicts_train))

print('valid:')
print(accuracy_score(valid_y, predicts_valid))
