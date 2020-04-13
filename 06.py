def char_n_gram(str, n):
    return {str[i:i+n] for i in range(len(str) - n + 1)}

X = char_n_gram("paraparaparadise", 2)
Y = char_n_gram("paragraph", 2)

print("X =", X)
print("Y =", Y)

union = X | Y
print("X | Y =", union)

intersection = X & Y
print("X & Y =", intersection)

difference1 = X - Y
print("X - Y =", difference1)
difference2 = Y - X
print("Y - X =", difference2)

print("'se' in X? ->", "se" in X)
print("'se' in Y? ->", "se" in Y)
