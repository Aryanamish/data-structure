# reverse the given string

from __init__ import performance
import string
import random


@performance
def reverse_string(something):
    reverse = ''
    length = len(something)
    for i in range(length-1, -1, -1):
        reverse += something[i]
    return reverse

@performance
def reverse_string2(something):
    return something[-1::-1]

@performance
def reverse_string3(something):
    something = something.split()
    something.reverse()
    return "".join(something)

some_string = ''.join(random.choices(string.ascii_uppercase + string.digits + ' ', k = 10000000))
# reverse_string(some_string)
reverse_string2(some_string)
reverse_string3(some_string)
