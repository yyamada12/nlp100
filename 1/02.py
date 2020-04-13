str1 = "パトカー"
str2 = "タクシー"
mixed = ""
for c1, c2 in zip(str1, str2) :
    mixed += c1 + c2
print(mixed)