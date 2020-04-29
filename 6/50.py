import pandas as pd
from sklearn.model_selection import train_test_split

df = pd.read_table('./NewsAggregatorDataset/newsCorpora.csv', names=[
                   'ID', 'TITLE', 'URL', 'PUBLISHER', 'CATEGORY', 'STORY', 'HOSTNAME', 'TIMESTAMP'])
extracted_df = df[df['PUBLISHER'].isin([
    'Reuters', 'Huffington Post', 'Businessweek', 'Contactmusic.com', 'Daily Mail'])]
train_df, valid_and_test_df = train_test_split(
    extracted_df, test_size=0.2, random_state=0)
valid_df, test_df = train_test_split(
    valid_and_test_df, test_size=0.5, random_state=0)
train_df.to_csv('train.txt', index=None, sep='\t')
valid_df.to_csv('valid.txt', index=None, sep='\t')
test_df.to_csv('test.txt', index=None, sep='\t')
