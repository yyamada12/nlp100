import joblib
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import pandas as pd
from tqdm import tqdm


train_X = pd.read_table('train.feature.txt')
train_y = pd.read_table('train.label.txt')

valid_X = pd.read_table('valid.feature.txt')
valid_y = pd.read_table('valid.label.txt')

test_X = pd.read_table('test.feature.txt')
test_y = pd.read_table('test.label.txt')


Cs = [0.001, 0.01, 0.1, 1, 10, 100, 1000]
train_results = []
valid_results = []
test_results = []
for C in tqdm(Cs):
    lr = LogisticRegression(random_state=0, C=C)
    lr.fit(train_X, train_y['CATEGORY'])
    predicts_train = lr.predict(train_X)
    predicts_valid = lr.predict(valid_X)
    predicts_test = lr.predict(test_X)

    train_results.append(accuracy_score(train_y, predicts_train))
    valid_results.append(accuracy_score(valid_y, predicts_valid))
    test_results.append(accuracy_score(test_y, predicts_test))


ax = plt.gca()
ax.set_xlabel('C')
ax.set_ylabel('precision')
ax.set_xscale('log')
ax.plot(Cs, train_results, label='train')
ax.plot(Cs, valid_results, label='valid')
ax.plot(Cs, test_results, label='test')
ax.legend()

plt.savefig('58.png')
