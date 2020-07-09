import sys
N = int(input())

count_nums = [0] * 10001
for i in range(N):
    count_nums[int(sys.stdin.readline().rstrip())] += 1

for i in range(10001):
    sys.stdout.write('%s\n' % i*count_nums[i])
