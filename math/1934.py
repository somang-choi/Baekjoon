import sys

def calc_gcd(a, b):
    while b != 0:
        a = a % b
        a, b = b, a
    return a

def calc_lcm(a, b):
    gcd = calc_gcd(a, b)
    return a*b//gcd

T = int(sys.stdin.readline().rstrip())
for i in range(T):
    A, B = map(int, sys.stdin.readline().rstrip().split())
    sys.stdout.write('%d\n' % calc_lcm(A, B))