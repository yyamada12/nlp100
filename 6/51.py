import category_encoders as ce
import gc
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer


def trans(series, vectorizer, suffix):
    vec = vectorizer.transform(series)
    return pd.DataFrame(
        vec.toarray(), columns=vectorizer.get_feature_names()).add_suffix(suffix)


def make_feature(df, ohe, vec_tfidf):
    """PUBLISHER と TITLEのTFIDFVector を特徴量として返す

    Args:
        df (DataFrame): 元となるDataFrame
        ohe (OneHotEncoder): fit済みのOneHotEncoder
        vec_tfidf (TfidfVectorizer): fit済みのTfidfVectorizer

    Returns:
        pd.DataFrame: 特徴量のDataFrame
    """

    publisher_df = ohe.transform(pd.DataFrame(df['PUBLISHER']))
    title_df = trans(df['TITLE'], vec_tfidf, '_tfidf')
    return pd.concat([publisher_df, title_df], axis=1)


train_df = pd.read_table('./train.txt')

ce_ohe = ce.OneHotEncoder(cols='PUBLISHER')
ce_ohe.fit(pd.DataFrame(train_df['PUBLISHER']))

vec_tfidf = TfidfVectorizer()
vec_tfidf.fit(train_df['TITLE'])

train_feature_df = make_feature(train_df, ce_ohe, vec_tfidf)
train_feature_df.to_csv('train.feature.txt', index=None, sep='\t')
train_df['CATEGORY'].to_csv(
    'train.label.txt', index=None, sep='\t')

del train_feature_df
del train_df
gc.collect()

for data in ['valid', 'test']:
    df = pd.read_table('./' + data + '.txt')
    feature_df = make_feature(df, ce_ohe, vec_tfidf)
    feature_df.to_csv(data + '.feature.txt', index=None, sep='\t')
    df['CATEGORY'].to_csv(data + '.label.txt', index=None, sep='\t')
