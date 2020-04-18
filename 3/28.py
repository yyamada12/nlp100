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


class Text:
    def __init__(self, text):
        self.text = text

    def remove_emphasis(self):
        return Text(re.sub(r"'{2,}", "", self.text))

    def remove_inner_link(self):
        return Text(re.sub(
            r"\[\[(?:[^\|]*\|)??(([^\|]*?)|({{.*?}}))\]\]", r"\1", self.text))

    def remove_file(self):
        return Text(re.sub(r"\[\[ファイル:(?:[^\|]*\|)*?([^\|]*?)\]\]", r"\1", self.text))

    def remove_template_lang(self):
        return Text(re.sub(r"{{(?:[^\|]*\|)*?([^\|]*?)}}", r"\1", self.text))

    def remove_outer_link(self):
        return Text(re.sub(r"\[(?:[\w&:/%\=\.\?]*)(.*?)\]", r"\1", self.text))

    def remove_tag(self):
        return Text(re.sub(r"<.*?>", "", self.text))


basic_info_dict = {}
for key, value in basic_infos:
    text = Text(value)\
        .remove_emphasis()\
        .remove_inner_link()\
        .remove_file()\
        .remove_template_lang()\
        .remove_outer_link()\
        .remove_tag()\
        .text
    basic_info_dict[key] = text
    print("'" + key + "', " + "'" + text + "'")
