s = list(input())
count = len(s)//10 + 1
for i in range(count):
    start = i*10
    end = start + 10
    print(''.join(s[start:end]))