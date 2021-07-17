'''
Create your own Hash Table in python
'''

class HashTable:
    def __init__(self, size) -> None:
        self.__size = size
        self.data = [[] for i in range(size)]
        self.length = 0

    def set(self, key, value):
        location = self._hash(key)
        inserted = False
        if len(self.data[location]) != 0:
            for i in self.data[location]:
                if i[0] == key:
                    self.data[location][1] = value
                    inserted = True
        if inserted is False:
            self.data[location].append([key, value])
        self.length += 1
        return value

    def get(self, key, return_val=None):
        location = self._hash(key)
        if len(self.data[location]) != []:
            for i in self.data[location]:
                if i[0] == key:
                    return i[1]
        return return_val

    def delete(self, key):
        location = self._hash(key)
        if len(self.data[location]) != []:
            for i in self.data[location]:
                if i[0] == key:
                    del i
                    self.length -= 1
        return None

    def _hash(self, key):
        key = str(key)
        hash_sum = 0
        for i in key:
            hash_sum += ord(i)
        return hash_sum % self.__size

    def __setitem__(self, key, value):
        self.set(key, value)
    
    def __getitem__(self, key):
        return self.get(key, None)

    def __str__(self):
        array = ['{']
        for i in self.data:
            for j in i:
                array.append(f"{repr(j[0])}: {j[1]}")
                array.append(f", ")
        array.pop()
        array.append('}')
        return ''.join(array)

    def __repr__(self):
        return self.__str__() 

def abc():
    pass
my_hash = HashTable(50)
my_hash.set('hi', 123)
my_hash['hello'] = 11
my_hash[1] = True
print(my_hash['hi'])
print(my_hash)