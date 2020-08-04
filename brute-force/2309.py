dwarfs = []
for i in range(9):
    dwarfs.append(int(input()))

res = sum(dwarfs)
criminal = []
dwarfs.sort()

for i in range(9):
    for j in range(i+1, 9):
        if res - dwarfs[i] - dwarfs[j] == 100:
            criminal = [dwarfs[i], dwarfs[j]]
            break

dwarfs.remove(criminal[0])
dwarfs.remove(criminal[1])
print('\n'.join(list(map(str, dwarfs))))