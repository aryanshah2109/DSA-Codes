from typing import List
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        n = len(nums)

        ## BRUTE
        ## TC = O(n2) SC = O(1)
        # for i in range(n):            
        #     current_sum = 0
        #     for j in range(i, n):
        #         current_sum += nums[j]
        #         if j-i+1 >= 2 and current_sum % k == 0:
        #             return True        
        # return False


        ## Optimal
        ## TC = O(n) SC = O(n)
        hashmap = {0 : -1}
        current_sum = 0
        for i,x in enumerate(nums):
            current_sum += x
            remainder = current_sum % k
            if remainder not in hashmap:
                hashmap[remainder] = i
            elif i - hashmap[remainder] >= 2:
                return True
        return False