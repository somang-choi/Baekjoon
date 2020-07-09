N = int(input())
scores = []
for i in range(N):
    name, kor, eng, math = input().split(' ')
    scores.append((name, int(kor), int(eng), int(math)))

scores.sort(key = lambda x: (-int(x[1]), int(x[2]), (-int(x[3])), x[0]))
for s in scores:
    print(s[0])