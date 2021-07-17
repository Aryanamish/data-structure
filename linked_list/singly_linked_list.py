class Node:
    def __init__(self, value):
        self.value = value
        self.next_node = None
    def __str__(self):
        a = [self.value] + [self.next_node.value] if self.next_node is not None else []
        return f"{' -- > '.join(a)}"

    def __repr__(self):
        return repr(self.value)

class SingleLinkedList:
    Node = Node
    def __init__(self, value):
        self.head_node = Node(value)
        self.last_node = self.head_node
        self.length = 1

    def __get_nth_nodes__(self, index):
        if index < self.length:
            i = 0
            next_node = self.head_node
            while(i < index):
                next_node = next_node.next_node
                i += 1
            return next_node
        elif index >= self.length:
            raise IndexError("LinkedList index out of range")

    def append(self, value):
        self.last_node.next_node = self.Node(value)
        self.last_node = self.last_node.next_node
        self.length += 1
        return self.last_node
    def prepend(self, value):
        new_head = self.Node(value)
        new_head.next_node = self.head_node
        self.head_node = new_head
        self.length += 1

    def reverse(self):
        if self.length == 1:
            return None
        first = self.head_node
        second = first.next_node
        while second is not None:
            temp = second.next_node
            second.next_node = first
            first = second
            second = temp
        self.head_node, self.last_node = self.last_node, self.head_node



    def insert(self, index, value):
        if index == self.length:
            self.append(value)
        elif index == 0:
            self.prepend(value)
        else:
            node = self.__get_nth_nodes__(index-1)
            next_node = node.next_node
            node.next_node = Node(value)
            node.next_node.next_node = next_node
            self.length += 1

    def replace(self, index, value):
        node = self.__get_nth_nodes__(index)
        node.value = value

    def delete(self, index):
        if index == 0:
            deleted_node = self.head_node
            self.head_node = deleted_node.next_node
            self.length -= 1
        elif index >= self.length:
            raise IndexError("Listindex out of range")
        else:
            node = self.__get_nth_nodes__(index-1)
            deleted_node = node.next_node
            node.next_node = node.next_node.next_node
            self.length -= 1
        return deleted_node

    def get(self, index):
        return self.__get_nth_nodes__(index)

    def __getitem__(self, index):
        return self.__get_nth_nodes__(index).value
    
    def __setitem__(self, index, value):
        self.replace(index, value)

    def __get_all_value__(self):
        node = self.head_node
        values = [node.value]
        for _ in range(0, self.length-1):
            node = node.next_node
            values.append(node.value)
        return values


    def __str__(self):
        value = map(repr, self.__get_all_value__())
        return f"[{' --> '.join(value)}]"
    
    def __repr__(self):
        return self.__str__()

linked_list = SingleLinkedList(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)
linked_list.append(5)

linked_list.append(134)
print(linked_list)
linked_list.reverse()
print(linked_list)
# linked_list[2] = 'papa'

