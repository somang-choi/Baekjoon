import sys, datastructure

def deliminate(op):
    cmd = op[0]
    if cmd == 'push_front':
        deque.push_front(num=int(op[1]))
    elif cmd == 'push_back':
        deque.push_back(num=int(op[1]))
    elif cmd == 'pop_front':
        print(deque.pop_front())
    elif cmd == 'pop_back':
        print(deque.pop_back())
    elif cmd == 'size':
        print(deque.size())
    elif cmd == 'empty':
        print(deque.empty())
    elif cmd == 'front':
        print(deque.front())
    elif cmd == 'back':
        print(deque.back())

N = int(input())
deque = datastructure.Deque()
for i in range(N):
    deliminate(sys.stdin.readline().rstrip().split(' '))