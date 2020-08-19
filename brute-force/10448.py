from math import sqrt
from itertools import combinations

def solve():
    K = int(input())
    end = int(0.5*(sqrt(1 + 8*K) - 1)) + 1

    triangulars = []
    for i in range(1, end):
        t = int(i*(i+1)/2)
        triangulars.append(t)

    triangulars = triangulars*3

    result = 0
    for combi in combinations(triangulars, 3):
        if sum(combi) == K:
            result = 1
            break

    print(result)

T = int(input())
for t in range(T):
    solve()