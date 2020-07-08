import sys

N = int(input())
coords = []
for i in range(N):
    x, y = map(int, sys.stdin.readline().rstrip().split(' '))
    coords.append((x, y))

coords = sorted(coords)
for (x, y) in coords:
    print(x, y)