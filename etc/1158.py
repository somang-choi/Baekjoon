N, K = map(int, input().split())
people = list(range(1, N + 1))
result = []
index = K - 1

while True:
    result.append(people.pop(index))
    if not people:
        break
    index = (index + K - 1) % len(people)

print('<' + ', '.join(map(str, result)) + '>')