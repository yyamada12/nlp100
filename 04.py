sentence = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."

words = sentence.replace(',', '').replace('.', '').split()
word_map = {}
for i, word in enumerate(words):
    if i in [1, 5, 6, 7, 8, 9, 15, 16, 19]:
        word_map[word[0]] = i
    else:
        word_map[word[:2]] = i

print(word_map)