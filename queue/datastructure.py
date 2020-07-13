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

class Deque:
    def __init__(self):
        self.len = 0
        self.list = []
    
    def push_front(self, num):
        self.list.insert(0, num)
        self.len += 1

    def push_back(self, num):
        self.list.append(num)
        self.len += 1

    def pop_front(self):
        if self.len == 0:
            return -1
        result = self.list[0]
        del self.list[0]
        self.len -= 1
        return result
    
    def pop_back(self):
        if self.len == 0:
            return -1
        last_index = self.len -1
        result = self.list[last_index]
        del self.list[last_index]
        self.len -= 1
        return result
    
    def size(self):
        return self.len

    def empty(self):
        return 1 if self.len == 0 else 0
    
    def front(self):
        return self.list[0] if self.len != 0 else -1
    
    def back(self):
        return self.list[-1] if self.len != 0 else -1
