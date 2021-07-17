class Q:
    class Node:
        def __init__(self, value, next_node=None):
            self.value = value
            self.next = next_node

    def __init__(self) -> None:
        self.first = None
        self.last = None
        self.length = 0
    
    def enqueue(self, value):
        new_node = self.Node(value, None)
        if self.first is None:
            self.first = new_node
        else:
            self.last.next = new_node
        self.last = new_node
        self.length += 1

    def dequeue(self):
        first_in_line = self.first
        self.first = first_in_line.next
        self.length -= 1
        return first_in_line.value

    def peek(self):
        return self.first.value if self.first is not None else None
    
    def isEmpty(self):
        return True if self.length == 0 else False
    
    def __get__all_values__(self):
        node = self.first
        values = []
        while node is not None:
            values.append(node.value)
            node = node.next
        return values

    def __str__(self):
        value = map(repr, self.__get__all_values__())
        return f"< {'--> '.join(value)} >"

q = Q()
print(q.peek())
q.enqueue(129)
q.enqueue(1242)
q.enqueue('aryan')
q.enqueue('amish')
print(q)
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q)









