# Return true if the permutation of pattern string is found in string s
# Eg: s = "ofrbanva" ,  pattern = "ab"
# permutation of ab -> ab, ba
# "ba" exists in s so return True

# Eg: s = "ofrbcnva" ,  pattern = "ab"
# permutation of ab -> ab, ba
# "ba" or "ab" does not exist in s so return False

import numpy as np

# TC = O(n) SC = O(1)
def permutation(s: str, part: str) -> str:

    freq = np.zeros(26)
    window = np.zeros(26)

    for char in part:
        freq[ord(char) - 97] += 1

    i = 0
    j = 0
    k = len(part)
    n = len(s)
    
    i = 0
    for j in range(n):
        # add right char
        window[ord(s[j]) - 97] += 1

        # shrink window if size > k
        if j - i + 1 > k:
            window[ord(s[i]) - 97] -= 1
            i += 1

        # compare when window size == k
        if j - i + 1 == k:
            if np.array_equal(freq, window):
                return True

    return False

print(permutation("ofrbanva", "ab"))
print(permutation("ofrbanva", "bc"))