import sys, datastructure

def deliminate(op):
    cmd = op[0]
    if cmd == 'push':
        queue.push(num=int(op[1]))
    elif cmd == 'pop':
        print(queue.pop())
    elif cmd == 'size':
        print(queue.size())
    elif cmd == 'empty':
        print(queue.empty())
    elif cmd == 'front':
        print(queue.front())
    elif cmd == 'back':
        print(queue.back())

N = int(input())
queue = datastructure.Queue()
for i in range(N):
    deliminate(sys.stdin.readline().rstrip().split(' '))