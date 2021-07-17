'''
Given two sorted array in ascending order
write a program to add the two array and sort the array in ascending order
'''
from __init__ import performance
import random

a = [random.randint(1, 1000) for _ in range(10000000)]
b = [random.randint(1, 1000) for _ in range(100000)]
a.sort()
b.sort()

@performance
def add_sorted_array(array1, array2):
    array3 = array1 + array2
    array3.sort()
    return array3

@performance
def add_sorted_array2(array1, array2):
    array1_item = array1[0]
    index1 = 1
    array2_item = array2[0]
    index2 = 1
    a1_len = len(array1)
    a2_len = len(array2)
    new_array = list()
    while array1_item is not None or array2_item is not None:
        if (array1_item is not None and array2_item is not None and array1_item < array2_item) or array2_item is None:
            new_array.append(array1_item)
            if index1 == a1_len:
                array1_item = None
            else:
                array1_item = array1[index1]
                index1 += 1
        else:
            new_array.append(array2_item)
            if index2 == a2_len:
                array2_item = None
            else:
                array2_item = array2[index2]
                index2 += 1
    return new_array



# add_sorted_array(a,b)
add_sorted_array2(a, b)