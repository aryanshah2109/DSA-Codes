# Find out first non repeating character from string
# If not found return -1
# Eg: aabbccde -> First Non Repeating Character = "d" so Return "d"
# Eg: aabb -> No Non Repeating Character so return -1


import numpy as np

# TC = O(n2) SC = O(1)
def approach1(s):
    n = len(s)

    for i in range(n):
        isUnique = True

        for j in range(n):
            if s[i] == s[j] and i!=j :
                isUnique = False
        
        if isUnique == True:
            return s[i]
    
    return -1

# TC = O(n) SC = O(26) -> O(1)
def approach2(s):
    n = len(s)

    frequency = np.zeros(26)

    for char in s:
        frequency[ord(char) - 97] += 1
    
    for i in range(26):
        if frequency[i] == 1:
            return chr(97+i)
    return -1


s = input("Enter string: ")
print(f"First non repeating character: {approach1(s)}")
print(f"First non repeating character: {approach2(s)}")