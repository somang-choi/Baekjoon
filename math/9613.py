import sys

def calc_gcd(a, b):
    while b != 0:
        a = a % b
        a, b = b, a
    return a

def solve():
    nums = list(map(int, sys.stdin.readline().rstrip().split()))
    n = nums[0]
    numbers = nums[1:]
    gcds = []
    for i in range(n-1):
        current = numbers[i]
        afters = numbers[(i+1):n]
        while afters:
            gcd = calc_gcd(current, afters.pop())
            gcds.append(gcd)

    sys.stdout.write('%d\n' % sum(gcds))

t = int(input())
for i in range(t):
    solve()
