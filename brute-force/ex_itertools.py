import itertools

chars = ['A', 'B', 'C']

p = itertools.permutations(chars, 2)
c = itertools.combinations(chars, 2)

print(list(p))
print(list(c))