import string
lowers = list(string.ascii_lowercase)
uppers = list(string.ascii_uppercase)

words = list(input())
rot13 = words
for i in range(len(words)):
    w = words[i]
    if w.isupper():
        index = uppers.index(w) + 13 - 26
        rot13[i] = uppers[index]
    elif w.islower():
        index = lowers.index(w) + 13 - 26
        rot13[i] = lowers[index]

print(''.join(rot13))