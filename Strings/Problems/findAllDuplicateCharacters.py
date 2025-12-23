# Return all the duplicate characters in the input string
# Eg: aabccedd -> acd

import numpy as np

# TC = O(n2) SC = O(n)
def approach1(s):
    duplicates = ""

    for i in range(len(s)):
        isDuplicate = False

        for j in range(len(s)):

            if s[i] == s[j] and i!=j:
                isDuplicate = True
        
        if isDuplicate and s[i] not in duplicates:
            duplicates = duplicates + s[i]


    return duplicates

# TC = O(n + k) SC = O(n + k) for k unique characters in s
def approach2(s):
    n = len(s)

    hashmap = {}
    duplicates = ""

    for char in s:
        if char in hashmap:
            hashmap[char] += 1
        else:
            hashmap[char] = 1

    for key in hashmap.keys():
        if hashmap[key] > 1:
            duplicates = duplicates + key

    return duplicates

s = input("Enter string: ")

print(approach1(s))
print(approach2(s))