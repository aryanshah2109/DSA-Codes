# Print the length of the substring with only unique characters and no repeating characters
# Eg: "abdeaabd" -> 4 -> "abde"


import numpy as np


# TC = O(n2) SC = O(1)
def approach1(s:str):
    n = len(s)
    max_len = 0

    map_s = np.zeros(128)

    for i in range(n):
        map_s = np.zeros(128)

        for j in range(i,n):
            idx = ord(s[j])
            
            if map_s[idx] == 1:
                break

            map_s[idx] += 1

            substr_len = j - i + 1 

            max_len = max(max_len, substr_len)

    return max_len

# TC = O(n) SC = O(n)
def approach2(s:str):
    max_len = 0
    n = len(s)
    hashmap = {}

    left = 0

    for right in range(len(s)):
        if s[right] in hashmap:
            left = max(left, hashmap[s[right]] + 1)

        hashmap[s[right]] = right
        max_len = max(max_len, right - left + 1)

    
    return max_len


print(approach1("abdexabd"))
print(approach2("abdexabd"))