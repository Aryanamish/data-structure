'''
Given a array a = [1,2,3,5,6,2]
the function should return first recurring item i.e 2

a = [1,2,3,5,6,5]
return value should be 5

a = [1,2,3,5,6,10]
return value should be None 

Exception
a = [1,2,4,5,5,2,9]
here 2,2 are occuring and 5,5 are also reoccuring which one to return
'''
from __init__ import performance

@performance
def return_recurring_char(array):
    seen = set()
    for i in array:
        if i in seen:
            return i
        else:
            seen.add(i)
    return None

@performance
def return_first_recurring_char(array):
    seen = set()
    backup = None
    for i in array:
        if backup is None:
            if i in seen:
                backup = i
            else:
                seen.add(i)
        else:
            if i in seen:
                return i
            else:
                pass
    return backup



# a = [i for i in range(10000000)] + [-1]
a = [1,2,4,5,5,2,9]
print(return_recurring_char(a))
print(return_first_recurring_char(a))