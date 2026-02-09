from typing import List
from collections import defaultdict
class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        n = len(nums)

        ## Brute
        ## TC = O(n3) SC = O(n)
        # max_len = 0
        # for i in range(n):
            
        #     char_hash = {}
        #     for j in range(i, n):
        #         if nums[j] in char_hash:
        #             char_hash[nums[j]] += 1
        #         else:
        #             char_hash[nums[j]] = 1
                
        #         valid_candidate = True 
        #         for key, value in char_hash.items():
        #             if value != k:
        #                 valid_candidate = False
        #         if valid_candidate:
        #             max_len = max(max_len, j-i+1)
        # return max_len


        ## Optimal
        ## TC = O(n) SC = O(n)
        i = 0
        j = 0
        max_len = 0

        hashmap = defaultdict(int)

        while j < n:
            hashmap[nums[j]] += 1

            while hashmap[nums[j]] > k:
                hashmap[nums[i]] -= 1
                i += 1 

            max_len = max(max_len, j-i+1)
            j += 1

        return max_len

        


                

