'''
Given a large array and a sum
find out if the given array has two pairs of numeber whose sum is equal to the given sum
'''

from __init__ import performance

a = [1 for i in range(10000)]
b = [1 for _ in range(10000)] + [4, 4]



@performance
def find_sum_pair(array, total_sum):
    for i in array:
        for j in range(i,len(array)):
            if i + array[j] == total_sum:
                return True
    return False

@performance
def find_sum_pair2(array, total_sum):
    comp = set()
    for i in array:
        print(i)
        if i in comp:
            return True
        comp.add(total_sum - i)
    return False

# print(find_sum_pair(a, 8))
print(find_sum_pair2(b, 8))