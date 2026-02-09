import numpy as np
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        n = len(s)

        ## Brute
        ## TC = O(n2) SC = O(n)
        # max_len = 0      
        # for i in range(n):
        #     current_len = 0
        #     tracked = set()
        #     for j in range(i, n):
        #         if s[j] not in tracked:
        #             tracked.add(s[j])
        #             current_len += 1
        #         else: 
        #             break
        #         max_len = max(max_len, current_len)
        # return max_len


        ## Better
        ## TC = O(n2) SC = O(1)
        # max_len = 0      
        # for i in range(n):
        #     char_array = np.zeros(256)
        #     current_len = 0
        #     for j in range(i, n):
        #         if char_array[ord(s[j]) - 255] == 0:
        #             char_array[ord(s[j]) - 255] += 1
        #             current_len += 1
        #         else: 
        #             break
        #         max_len = max(max_len, current_len)
        # return max_len


        ## Optimal
        max_len = 0
        i = 0
        j = 0
        char_map = {}
        while j < n:
            if s[j] in char_map:
                char_map[s[j]] += 1
            else:
                char_map[s[j]] = 1
            
            while len(list(char_map.keys())) < j - i + 1:
                char_map[s[i]] -= 1
                if char_map[s[i]] == 0:
                    del char_map[s[i]]
                i += 1
                
            if len(list(char_map.keys())) == j - i + 1:
                max_len = max(max_len, j-i+1)
                
                j += 1

        return max_len
        

