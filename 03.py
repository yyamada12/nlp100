sentence = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."

words = sentence.replace(',','').replace('.', '').split()
len_list = list(map(lambda word: len(word), words))
print(len_list)

len_list2 = [len(word) for word in words]
print(len_list2)

len_list3 = list(map(lambda word: len(word.rstrip(',.')), sentence.split()))
print(len_list3)

len_list4 = [len(word.rstrip(',.')) for word in sentence.split()]
print(len_list4)
