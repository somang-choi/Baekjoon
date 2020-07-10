class Stack:
    def __init__(self):
        self.len = 0
        self.list = []

    def push(self, num):
        self.list.append(num)
        self.len += 1

    def pop(self):
        if self.size() == 0:
            return -1
        last_index = self.len - 1
        pop_result = self.list[last_index]
        del self.list[last_index]
        self.len -= 1
        return pop_result
    
    def size(self):
        return self.len
    
    def empty(self):
        return 1 if self.len == 0 else 0
    
    def top(self):
        return self.list[-1] if self.size() != 0 else -1
