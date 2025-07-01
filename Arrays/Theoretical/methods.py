'''
Array methods:
append()
count()
extend()
fromlist()
index()
insert()
pop()
remove()
reverse()
tolist()
'''

from array import *
a = array('i',[1,3,4,5,-4])

a.append(4)
a.append(-9)
print("After appending: ",a)

print(f"Count of 4: {a.count(4)}")
print(f"Count of -19: {a.count(-19)}")

print(f"Index of element 3: {a.index(3)}")
# print(f"Index of element 3: {a.index(-19)}") error if element not present

print(f"Popped element: {a.pop()}")   
print(f"Array after poping last element: {a}")
# if pop() has no arguments, it removes last element

print(f"Popped element: {a.pop(1)}")   
print(f"Array after poping element at index 1: {a}")
# if it has an argument like pop(3) it removes element at index 3

# a.remove does the same but it needs element in its arguments 
# instead of index