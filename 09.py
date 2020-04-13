

import random

def shuffle_long_words_of_sentence(str):
    def shuffle_long_word(word):
        if len(word) <= 4:
            return word
        else:
            first_chr = word[0]
            middle_chrs = word[1:-1]
            end_chr = word[-1]
            shuffled_middle_chrs = ''.join(random.sample(middle_chrs, len(middle_chrs)))
            return first_chr + shuffled_middle_chrs + end_chr

    return ' '.join(shuffle_long_word(word) for word in str.split())

print(shuffle_long_words_of_sentence("I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind ."))