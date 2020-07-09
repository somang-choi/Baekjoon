import sys
N, K = map(int, input().split(' '))
nums = list(map(int, sys.stdin.readline().rstrip().split(' ')))
nums.sort()
print(nums[K-1])