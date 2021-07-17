class Stack:
        
    def __init__(self) -> None:
        self.data = list()

    @property
    def length(self):
        return len(self.data)

    def push(self, value):
        self.data.append(value)

    def pop(self):
        return self.data.pop()
    
    def peek(self):
        return self.data[-1]

    def empty(self):
        return True if self.length == 0 else False

    def __str__(self) -> str:
        data = map(repr, self.data)
        return f"{'=> '.join(data)}"
        
if __name__ == '__main__':
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    print(s)
    s.pop()
    print(s)
    print(s.peek())