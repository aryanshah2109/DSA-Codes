# no built in array dtype
# we can use arrays either by numpy library or by important array module

from array import *

# declaration format: a = array('code',[elements])
# we can keep [] empty initially if we want

a1 = array('i',[2,4,5,-1])
print(type(a1))
print(a1)

print("Access via elements:")
for x in a1:
    print(x)

print("Access via index:")
for i in range(len(a1)):
    print(a1[i])

