def greedy(ropes):
    ropes.sort(reverse=True)
    weights = []
    for i in range(len(ropes)):
        w = ropes[i] * (i + 1)
        weights.append(w)
    return max(weights)

n = int(input())
ropes = []
for i in range(n):
    ropes.append(int(input()))
print(greedy(ropes))