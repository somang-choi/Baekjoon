import string, sys

chars = list(input().rstrip())
count_chars = [0] * 26

for c in chars:
    count_chars[ord(c) - 97] += 1

for c in count_chars:
    sys.stdout.write('%s ' % str(c))
