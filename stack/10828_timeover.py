stack = []
def push(x):
    stack.append(x)

def pop():
    if len(stack) == 0:
        print(-1)
    else:
        print(stack.pop())

def size():
    print(len(stack))

def empty():
    if len(stack) == 0:
        print(1)
    else:
        print(0)

def top():
    if len(stack) == 0:
        print(-1)
    else:
        print(stack[-1])

def deliminate(cmd):
    if 'push' in cmd:
        push(cmd.split(' ')[1])
    if cmd == 'pop':
        pop()
    if cmd == 'size':
        size()
    if cmd == 'empty':
        empty()
    if cmd == 'top':
        top()

N = int(input())
for i in range(N):
    deliminate(input())
