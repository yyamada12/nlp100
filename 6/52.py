import joblib
from sklearn.linear_model import LogisticRegression
import pandas as pd


train_X = pd.read_table('train.feature.txt', header=None)
train_y = pd.read_table('train.label.txt', header=None)

lr = LogisticRegression(random_state=0)
lr.fit(train_X, train_y[0])
joblib.dump(lr, '52.Joblib')
