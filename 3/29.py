import json
import gzip
import re
import requests

with gzip.open('jawiki-country.json.gz') as rf:
    for line in rf:
        obj = json.loads(line)
        if obj['title'] == 'イギリス':
            text = obj['text']
            break
basic_info_string = re.search(r'{{基礎情報.*?(.*)^}}$', text,
                              flags=(re.MULTILINE | re.DOTALL))
basic_infos = re.findall(r'^\|(.*?) *\= *(.*?) *(?:(?=\n\|)|(?=\n$))',
                         basic_info_string.group(1), flags=(re.MULTILINE | re.DOTALL))


for key, value in basic_infos:
    if key == '国旗画像':
        response = requests.get(
            'https://www.mediawiki.org/w/api.php?action=query&format=json&prop=imageinfo&iiprop=url&titles=File%3A' + value)
        print(response.json()['query']['pages']['-1']['imageinfo'][0]['url'])
        break
