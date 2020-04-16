import json
import gzip
import re

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

basic_info_dict = {}
for key, value in basic_infos:
    no_emphasis_value = re.sub(r"'{2,}", "", value)
    basic_info_dict[key] = no_emphasis_value
    print("'" + key + "', " + "'" + no_emphasis_value + "'")
