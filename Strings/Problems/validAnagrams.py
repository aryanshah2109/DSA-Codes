# Find out whether 2 strings are anagrams or not
# Anagrams are strings that become equal after rearranging their characters

import numpy as np

# Approach 1: Sort both. If sorted are equal, return True else False        
# TC = O(nlogn + mlogm) SC = O(n+m)    
def approach1(s,t):

    if len(s) != len(t):
        return False

    sorted_s = "".join(sorted(s))
    sorted_t = "".join(sorted(t))

    return sorted_s == sorted_t

# Approach 2: Create a array of 26 length. each element represents an alphabet
# Iterate through s and increase count in array. Iterate through t and decrease count
# in array. If there is a non zero value left in array, return False else True
# TC = O(n + m) SC = O(26) -> O(1)

def approach2(s,t):

    if len(s) != len(t):
        return False

    count_arr = np.zeros(26)

    for char in s:
        count_arr[ord(char) - 97] += 1

    for char in t:
        count_arr[ord(char) - 97] -= 1

    for element in count_arr:
        if element != 0:
            return False
        
    return True

        
print(approach1("arc","car"))
print(approach2("arc","car"))
        
print(approach1("ace","car"))
print(approach2("ace","car"))

