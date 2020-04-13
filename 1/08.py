def cipher(str):
    def transform(char):
        return chr(219 - ord(char)) if char.islower() else char
        
    return ''.join(transform(char) for char in str)

sentence = "I am an NLPer!!"

encrypted  = cipher(sentence)
print(encrypted)

decrypted = cipher(encrypted)
print(decrypted)
