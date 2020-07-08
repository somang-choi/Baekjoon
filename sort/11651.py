import sys

N = int(input())
coords = []
for i in range(N):
    x, y = map(int, sys.stdin.readline().rstrip().split(' '))
    coords.append((x, y))

coords = sorted(coords, key=lambda x : (x[1], x[0]))
for (x, y) in coords:
    print(x, y)