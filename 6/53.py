import joblib
import pandas as pd


valid_X = pd.read_table('valid.feature.txt')
valid_y = pd.read_table('valid.label.txt')

lr = joblib.load('52.Joblib')
predicts = lr.predict(valid_X)
probas = lr.predict_proba(valid_X)
df = pd.concat([pd.DataFrame({'predict': predicts}), pd.DataFrame(
    probas, columns=['b', 'e', 'm', 't'])], axis=1)
df.to_csv('53.txt', index=None, sep='\t')
