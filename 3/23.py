import json
import gzip
import re

with gzip.open('jawiki-country.json.gz') as rf:
    for line in rf:
        obj = json.loads(line)
        if obj['title'] == 'イギリス':
            text = obj['text']
            break
sections = re.findall(r'(={2,})(.*?)(={2,})', text)
for section in sections:
    print(section[1] + " " + str(int(len(section[0]) - 1)))
