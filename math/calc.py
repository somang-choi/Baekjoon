def calc_gcd(a, b):
    while b != 0:
        a = a % b
        a, b = b, a
    return a

def calc_lcm(a, b):
    gcd = calc_gcd(a, b)
    return a*b//gcd
