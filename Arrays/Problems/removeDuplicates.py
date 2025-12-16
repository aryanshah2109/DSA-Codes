import numpy as np

def removeDuplicatesBrute(arr):
    arr2 = []

    for i in arr:
        if(i not in arr2):
            arr2.append(i)
    return arr2


def removeDuplicatesDictionary(arr):
    temp = {}

    for i in range(0,len(arr)):
        if arr[i] not in temp.keys():
            temp.update({arr[i]:0})
    
    return list(temp.keys())

def removeDuplicatesSet(arr):
    return list(set(arr))

arr = np.array([])
n = int(input("Enter size: "))
arr = np.fromstring(input("Enter array elements: "),sep=' ',dtype=int)


arr2 = removeDuplicatesBrute(arr)
print(arr2)

arr3 = removeDuplicatesSet(arr)
print(arr3)

uniqueElements = removeDuplicatesDictionary(arr)
print(uniqueElements)