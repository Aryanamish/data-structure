class Stack:
    class Node:
        def __init__(self, value=None):
            self.value = value
            self.next = None

    def __init__(self) -> None:
        self.top = self.Node()
        self.bottom = self.top
        self.length = 0

    @property
    def peek(self):
        return self.top.value

    def push(self, value):
        if self.top.next is None:
            self.top.value = value
            self.top.next = self.Node()
        else:
            new_node = self.Node(value)
            new_node.next = self.top
            self.top = new_node
        self.length += 1

    @property
    def pop(self):
        pop = self.top
        self.top = self.top.next
        self.length -= 1
        return pop.value

    def __get_values__(self):
        node = self.top
        values = []
        while node.next is not None:
            values.append(node.value)
            node = node.next
        values.reverse()
        values = map(repr, values)
        return values
    @property
    def isEmpty(self):
        if self.length == 0:
            return True
        else:
            return False

    def __str__(self):
        return f'{"=> ".join(self.__get_values__())}'

s = Stack()
s.push(14)
s.push(15)
s.push(16)
s.push(17)
print(s)
print(s.pop)
print(s.pop)
print(s.pop)
print(s.pop)
print(s.peek)
s.push('hi how are you')
s.push('hi my name is aryan')
print(s)
print(s.pop)
print(s)