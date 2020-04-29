import joblib
from sklearn.linear_model import LogisticRegression
import pandas as pd


train_X = pd.read_table('train.feature.txt')
train_y = pd.read_table('train.label.txt')

lr = LogisticRegression(random_state=0)
lr.fit(train_X, train_y['CATEGORY'])
joblib.dump(lr, '52.Joblib')
