import itertools

chars = ['A', 'B', 'C']

p = itertools.permutations(chars, 2)  # 순열
c = itertools.combinations(chars, 2)  # 조합

print(list(p))
print(list(c))