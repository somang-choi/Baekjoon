N = int(input())
sizes = []
for i in range(N):
    x, y = map(int, input().split())
    sizes.append((x, y))

for cs in sizes:
    rank = 1
    
    for ns in sizes:
        if (cs[0] != ns[0]) and (cs[1] != ns[1]):
            if (cs[0] < ns[0]) and (cs[1] < ns[1]):
                rank += 1

    print(rank)