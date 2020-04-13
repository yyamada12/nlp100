def char_n_gram(str, n):
    return [str[i:i+n] for i in range(len(str) - n + 1)]
def word_n_gram(str, n):
    splitted  = str.split()
    return [splitted[i:i+n] for i in range(len(splitted) - n + 1)]

sentence = "I am an NLPer"
print(char_n_gram(sentence, 2))
print(word_n_gram(sentence, 2))