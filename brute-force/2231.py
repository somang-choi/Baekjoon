N = int(input())
result = 0
for i in range(1000001):
    nums = list(str(i))
    res = i
    for m in nums:
        res += int(m)
    if res == N:
        result = i
        break
print(result)