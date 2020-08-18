from itertools import combinations

N, S = map(int, input().split())
nums = list(map(int, input().split()))

count = 0
for i in range(1, N+1):
    for case in combinations(nums, i):
        if sum(case) == S:
            count += 1
print(count)
