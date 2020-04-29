import joblib
import pandas as pd
from sklearn.metrics import precision_score, recall_score, f1_score

train_X = pd.read_table('train.feature.txt')
train_y = pd.read_table('train.label.txt')

valid_X = pd.read_table('valid.feature.txt')
valid_y = pd.read_table('valid.label.txt')

lr = joblib.load('52.Joblib')
predicts_train = lr.predict(train_X)
predicts_valid = lr.predict(valid_X)


def print_score(type, labels, y_true, y_pred, score):
    print(type + ': ')
    print(labels)
    print(score(y_true, y_pred, labels=labels, average=None))
    print(type + ' macro average: ', end="")
    print(score(y_true, y_pred, average='macro'))
    print(type + ' micro average: ', end="")
    print(score(y_true, y_pred, average='micro'))
    print()


labels = ['b', 'e', 'm', 't']
print('train')
for type, score in zip(['precision', 'recall', 'f1'], [precision_score, recall_score, f1_score]):
    print_score(type, labels, train_y, predicts_train, score)

print('valid')
for type, score in zip(['precision', 'recall', 'f1'], [precision_score, recall_score, f1_score]):
    print_score(type, labels, valid_y, predicts_valid, score)
