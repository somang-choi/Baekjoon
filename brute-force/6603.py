from itertools import combinations

while True:
    S = list(map(int, input().split()))
    k = S.pop(0)
    if S == []:
        break

    for case in combinations(S, 6):
        print(' '.join(map(str, case)))
    print()
