N = input()
digits = len(N)
result = 0
for i in range(1, digits):
    result += i * 9 * pow(10, i-1)

result = result + (int(N) - pow(10, digits-1) + 1) * digits
print(result)
