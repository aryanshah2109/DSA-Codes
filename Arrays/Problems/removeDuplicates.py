import numpy as np

arr = np.array([])
n = int(input("Enter size: "))
arr = np.fromstring(input("Enter array elements: "),sep=' ',dtype=int)

# arr2 = []

# for i in arr:
#     if(i not in arr2):
#         arr2.append(i)
# arr2 = np.array(arr2)
# print(arr2)

arr2_set = set()
for i in arr:
    arr2_set.add(i)
arr2 = np.array(arr2_set)
print(arr2)