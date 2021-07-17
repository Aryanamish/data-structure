'''
create a datatype which behaves like array
it should have delete, append functions
'''
class Array:
    def __init__(self, *args, **kwargs):
        self.length = 0
        self.data = {}
    
    def append(self, item):
        self.data[self.length] = item
        self.length += 1

    def pop(self):
        if self.length > 0:
            item = self.data[self.length - 1]
            del self.data[self.length-1]
            self.length -= 1
        return item

    def delete(self, index):
        if index < self.length:
            item = self.data[index]
            self.length -= 1
            for i in range(index, self.length):
                self.data[i] = self.data[i+1]
            del self.data[self.length]
            return item

    def __setitem__(self, index, value):
        if index < self.length:
            self.data[index] = value
        else:
            raise "Array index out of range"

    def __getitem__(self, index):
        return self.data[index]

    def __str__(self) -> str:
        string = "["
        for _, value in self.data.items():
            string += value + ', '
        string = string[:-2]
        string += "]"
        return string
    def __repr__(self) -> str:
        return self.__str__(self)

# a = Array()
# a.append('hi')
# a.append('how')
# a.append('are')
# a.append('you')
# a[0] = "aryan"
# # a.pop()
# a.delete(1)
# print(a.length)
# print(a)