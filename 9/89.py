import pandas as pd

for data in ['train', 'valid', 'test']:
    df = pd.read_table(data + '.txt')
    df = df[['ID', 'CATEGORY', 'PUBLISHER', 'TITLE']]
    df['PUBLISHER'] = 'a'
    if data == 'valid':
        data = 'dev'
    elif data == 'test':
        df['CATEGORY'].to_csv('./bert/data/test_label.tsv',
                              header=None, index=None, sep='\t')
        df = df[['ID', 'TITLE']]
    df.to_csv('bert/data/' + data + '.tsv', header=None, index=None, sep='\t')
