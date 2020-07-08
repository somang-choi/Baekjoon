N = int(input())

result = [0] * (N + 1)
result[1] = 0
for i in range(2, N + 1):
    result[i] = result[i-1] + 1
    if i % 3 == 0 and result[i//3] + 1 < result[i]:
        result[i] = result[i//3] + 1
    if i % 2 == 0 and result[i//2] + 1< result[i]:
        result[i] = result[i//2] + 1
        
print(result[N])