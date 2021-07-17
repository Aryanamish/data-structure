'''
Given two array find if anny character is common in the two arrays
'''

from __init__ import performance
import random

a = ['d' for i in range(10000)] + ['a']
b = ['c' for _ in range(10000)] + ['a']

@performance
def find_common(array1, array2):
    for i in array1:
        for j in array2:
            if i==j:
                return True
    return False

@performance
def find_common2(array1, array2):
    s = set()
    for i in array1:
        s.add(i)
    for i in array2:
        if i in s:
            return True
    return False


print(find_common(a,b))
print(find_common2(a,b))

