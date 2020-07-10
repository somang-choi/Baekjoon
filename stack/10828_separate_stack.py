import stack, sys

def deliminate(cmd):
    op = cmd[0]
    if op == 'push':
        stack.push(num=int(cmd[1]))
    if op == 'pop':
        print(stack.pop())
    if op == 'size':
        print(stack.size())
    if op == 'empty':
        print(stack.empty())
    if op == 'top':
        print(stack.top())

N = int(sys.stdin.readline().rstrip())
stack = stack.Stack()
for i in range(N):
    deliminate(sys.stdin.readline().rstrip().split())
