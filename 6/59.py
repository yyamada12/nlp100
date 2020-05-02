import gc
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

Cs = [1, 10, 100, 1000]
valid_results = {}
best_score = 0
# for solver in tqdm(['newton-cg', 'lbfgs', 'sag']):
#     valid_results[solver] = []
#     for C in tqdm(Cs, leave=False):
#         lr = LogisticRegression(random_state=0, C=C,
#                                 solver=solver, max_iter=100)
#         lr.fit(train_X, train_y['CATEGORY'])
#         predicts_valid = lr.predict(valid_X)
#         score = accuracy_score(valid_y, predicts_valid)
#         if score > best_score:
#             best_score = score
#             best_lr = lr
#         valid_results[solver].append(score)

for l1_ratio in tqdm([0, 0.25, 0.5, 0.75]):
    valid_results['saga_' + str(l1_ratio)] = []
    for C in tqdm(Cs, leave=False):
        lr = LogisticRegression(penalty='elasticnet', random_state=0,
                                C=C,  solver='saga', max_iter=5000, l1_ratio=l1_ratio)
        lr.fit(train_X, train_y['CATEGORY'])
        predicts_valid = lr.predict(valid_X)
        score = accuracy_score(valid_y, predicts_valid)
        if score > best_score:
            best_score = score
            best_lr = lr
        valid_results['saga_' + str(l1_ratio)].append(score)

del train_X, train_y, valid_X, valid_y
gc.collect()

test_X = pd.read_table('test.feature.txt')
test_y = pd.read_table('test.label.txt')

predicts_test = best_lr.predict(test_X)
score = accuracy_score(test_y, predicts_test)
print('best score: ' + str(score))

ax = plt.gca()
ax.set_xlabel('C')
ax.set_ylabel('precision')
ax.set_xscale('log')
for solver, results in valid_results.items():
    ax.plot(Cs, results, label=solver)
ax.legend()

plt.savefig('59.png')
