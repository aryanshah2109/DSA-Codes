import numpy as np
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        ## Brute
        ## TC = O(n* (k2 + k*logk)) = O(n*k2)
        ## SC = O(n)

        # n = len(s2)
        # k = len(s1)
        # i = 0
        # j = 0
        
        # sorted_t = "".join(sorted(s1))
        
        # for i in range(n-k+1):
        #     substr = ""
        #     for j in range(i, i+k):
        #         substr += s2[j]
        #     sorted_substr = "".join(sorted(substr))
        #     if sorted_substr == sorted_t:
        #         return True
        
        # return False


        ## Optimal
        ## TC = O(n*k)
        ## SC = O(1)

        s1_map = [0] * 26
        
        for char in s1:
            s1_map[ord(char) - 97] += 1
        
        n = len(s2)
        k = len(s1)
        for i in range(n-k+1):
            substr_map = [0] * 26
            for j in range(i, i+k):
                substr_map[ord(s2[j])-97] += 1
            
            isCandidate = True
            if substr_map == s1_map:
                return True

        return False