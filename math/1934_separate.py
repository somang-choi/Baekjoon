import calc, sys

T = int(sys.stdin.readline().rstrip())
for i in range(T):
    A, B = map(int, sys.stdin.readline().rstrip().split())
    sys.stdout.write('%d\n' % calc.calc_lcm(A, B))