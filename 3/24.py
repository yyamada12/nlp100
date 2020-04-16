import json
import gzip
import re

with gzip.open('jawiki-country.json.gz') as rf:
    for line in rf:
        obj = json.loads(line)
        if obj['title'] == 'イギリス':
            text = obj['text']
            break
mediafiles = re.findall(r'\[\[ファイル:(.*?)\|', text)
for mediafile in mediafiles:
    print(mediafile)
