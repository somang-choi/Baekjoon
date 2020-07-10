import sys

def isvps(ps):
    score = 0
    for p in ps:
        if p == '(':
            score += 1
        else:
            score -= 1
        if score == -1:
            break
        
    if score == 0:
        sys.stdout.write('YES\n')
    else:
        sys.stdout.write('NO\n')

T = int(sys.stdin.readline().rstrip())
for i in range(T):
    ps_list = list(sys.stdin.readline().rstrip())
    isvps(ps_list)
        
