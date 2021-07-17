class Node:
    def __init__(self, value, previous_node=None, next_node=None):
        self.value = value
        self.previous_node = previous_node
        self.next_node = next_node

    def __str__(self):
        return str(self.value)
    
    def __repr__(self):
        return repr(self.value)

class DoublyLinkedList:
    Node = Node

    def __init__(self, value):
        self.head = self.Node(value)
        self.tail = self.head
        self.length = 1

    def reverse(self):
        current_node = self.head
        while current_node is not None:
            temp = current_node.previous_node
            current_node.previous_node  = current_node.next_node
            current_node.next_node = temp
            current_node = current_node.previous_node


        self.tail , self.head = self.head, self.tail
        


    def lookup(self, index):
        if index >= self.length:
            raise IndexError("LinkedList index out of range")
        elif index <= self.length/2:
            i = 0
            current_node = self.head
            while(i < index):
                current_node = current_node.next_node
                i += 1
            return current_node
        elif index > self.length/2:
            i = self.length - 1
            current_node = self.tail
            while(i < index):
                current_node = current_node.previous_node
                i -= 1
            return current_node


    def append(self, value):
        self.tail.next_node = self.Node(value, self.tail)
        self.tail = self.tail.next_node
        self.length += 1

    def prepend(self, value):
        head = self.Node(value, None, self.head)
        self.head.previous_node = head
        self.head = head
        self.length += 1

    def insert(self, index, value):
        if index == 0:
            self.prepend(value)
            new_node = self.head
        elif index == self.length:
            self.append(value)
            new_node = self.tail
        else:
            parent_node = self.lookup(index-1)
            new_node = self.Node(value, parent_node, parent_node.next_node)
            parent_node.next_node = new_node
            self.length += 1
        return new_node

    def remove(self, index):
        if index == 0:
            deleted_node = self.head
            self.head = self.head.next_node
            self.head.previous_node = None
            
        elif index >= self.length:
            raise IndexError("Listindex out of range")
        else:
            deleted_node = self.lookup(index)
            parent_node = deleted_node.previous_node
            child_node = deleted_node.next_node
            parent_node.next_node = child_node
            if child_node is None:
                self.tail = parent_node
            else:
                child_node.previous_node = parent_node
        self.length -= 1
        return deleted_node
        
    def replace(self, index, value):
        self.lookup(index).value = value

    def __setitem__(self, index, value):
        self.replace(index, value)

    def __getitem__(self, index):
        return self.lookup(index).value

    def __get_all_value__(self):
        node = self.head
        values = [node.value]
        while(node.next_node is not None):
            node = node.next_node
            values.append(node.value)
        return values

    def __str__(self):
        value = map(repr, self.__get_all_value__())
        return f"[{' <--> '.join(value)}]"
    
    def __repr__(self):
        return self.__str__()


dll = DoublyLinkedList(17)
dll.append('hi')
dll.prepend('i am 18')
print(dll)
dll.reverse()
print(dll)