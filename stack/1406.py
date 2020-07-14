import sys
left_stack = list(sys.stdin.readline().rstrip())
right_stack = []

M = int(sys.stdin.readline().rstrip())
for i in range(M):
    cmd = sys.stdin.readline().rstrip().split()
    op = cmd[0]
    if op == 'L':
        if len(left_stack) != 0:
            poped = left_stack.pop()
            right_stack.append(poped)
    if op == 'D':
        if len(right_stack) != 0:
            poped = right_stack.pop()
            left_stack.append(poped)
    if op == 'B':
        if len(left_stack) != 0:
            left_stack.pop()
    if op == 'P':
        left_stack.append(cmd[1])

right_stack.reverse()
result = left_stack + right_stack
sys.stdout.write('%s\n' % ''.join(result))
