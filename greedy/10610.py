def greedy(n):
    if '0' not in n or int(n)%3 != 0:
        return -1
    
    return ''.join(sorted(n, reverse=True))

n = input()
print(greedy(n))