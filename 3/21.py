import json
import gzip
import re

with gzip.open('jawiki-country.json.gz') as rf:
    for line in rf:
        obj = json.loads(line)
        if obj['title'] == 'イギリス':
            text = obj['text']
            break
categories = re.findall(r'\[\[Category:.*\]\]', text)
for category in categories:
    print(category)
