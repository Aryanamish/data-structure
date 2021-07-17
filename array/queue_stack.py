from stack import Stack

class Q:
    def __init__(self) -> None:
        self.stack = Stack()
    
    def enqueue(self, value):
        self.stack.push(value)
    
    def dequeue(self):
        data = self.stack.data[0]
        self.stack.data.remove(data)
        return data

    def peek(self):
        return self.stack.data[0]
    
    def empty(self):
        return self.stack.empty
    
    def __str__(self):
        data = self.stack.data.copy()
        data.reverse()
        data = map(repr, data)
        return f'{"--> ".join(data)}'

q = Q()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)

print(q.dequeue())
print(q)