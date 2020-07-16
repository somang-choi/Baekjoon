def calc_gcd(a, b):
    while b != 0:
        a = a % b
        a, b = b, a
    return a

A, B = map(int, input().split())
result = '1' * calc_gcd(A, B)
print(result)