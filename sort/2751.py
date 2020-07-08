import sys

N = int(input())
nums = []
for i in range(N):
    nums.append(int(sys.stdin.readline().rstrip()))

print('\n'.join(list(map(str, sorted(nums)))))