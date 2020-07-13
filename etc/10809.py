import string, sys

chars = list(input().rstrip())
index_chars = [-1] * 26

for i in range(len(chars)):
    if index_chars[ord(chars[i]) - 97] == -1:
        index_chars[ord(chars[i]) - 97] = i

for c in index_chars:
    sys.stdout.write('%s ' % str(c))
