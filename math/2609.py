def calc_gcd(a, b):
    while b != 0:
        a = a % b
        a, b = b, a
    return a

def calc_lcm(a, b, gcd):
    return a*b//gcd

A, B = map(int, input().split())
GCD = calc_gcd(A, B)
LCM = calc_lcm(A, B, GCD)
print('%d\n%d' % (GCD, LCM))