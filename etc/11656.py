word = input()
len_word = len(word)
suffixes = [word]
for i in range(1, len_word):
    suffixes.append(word[i:len_word])
suffixes.sort()
print('\n'.join(suffixes))