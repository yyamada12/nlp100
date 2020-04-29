import joblib
import numpy as np
import pandas as pd

lr = joblib.load('52.Joblib')
with open('train.feature.txt') as f:
    cols = f.readline().rstrip('\n').split('\t')

coef_df = pd.DataFrame(lr.coef_, columns=cols)

for i, label in enumerate(lr.classes_):
    print(label)
    print('top 10 features: ')
    print(coef_df.sort_values(i, axis=1).iloc[0, -10:])
    print()
    print('bottom 10 features: ')
    print(coef_df.sort_values(i, axis=1).iloc[0, :10])
    print()
