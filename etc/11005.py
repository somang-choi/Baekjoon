import string
N, B = map(int, input().split())

numbers = string.digits + string.ascii_uppercase
result = []

while N != 0:
    result.append(numbers[N % B])
    N = N // B
print(''.join(reversed(result)))