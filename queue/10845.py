import sys

class Queue:
    def __init__(self):
        self.len = 0
        self.list = []
    
    def push(self, num):
        self.list.append(num)
        self.len += 1
    
    def pop(self):
        if self.size() == 0:
            return -1
        pop_result = self.list[0]
        del self.list[0]
        self.len -= 1
        return pop_result
    
    def size(self):
        return self.len

    def empty(self):
        return 1 if self.size() == 0 else 0
    
    def front(self):
        return self.list[0] if self.size() != 0 else -1
    
    def back(self):
        return self.list[-1] if self.size() != 0 else -1

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
queue = Queue()
for i in range(N):
    deliminate(sys.stdin.readline().rstrip().split(' '))