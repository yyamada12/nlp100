import spacy
from tqdm import tqdm

nlp = spacy.load('ja_ginza')

for data in ['train', 'dev', 'test']:
    print('processing kyoto-' + data + '.ja ...')
    with open('./kftt-data-1.0/data/orig/kyoto-' + data + '.ja') as rf, open('data90/' + data + '.ja', 'w') as wf:
        for line in tqdm(rf):
            doc = nlp(line)
            wf.write(
                ' '.join(token.text for sent in doc.sents for token in sent) + '\n')

for data in ['train', 'dev', 'test']:
    print('processing kyoto-' + data + '.en ...')
    with open('./kftt-data-1.0/data/orig/kyoto-' + data + '.en') as rf, open('data90/' + data + '.en', 'w') as wf:
        for line in tqdm(rf):
            wf.write(line.strip() + '\n')
