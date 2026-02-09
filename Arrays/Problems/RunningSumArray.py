import numpy as np
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ## Basically find the prefix sum of nums
        
        n = len(nums)   
        
        ## Brute
        ## TC = O(n2) SC = O(n)
        # sum_list = []
        # for i in range(n):
        #     sum_previous = 0
        #     for j in range(i, -1, -1):
        #         sum_previous += nums[j]
        #     sum_list.append(sum_previous)
        
        # return sum_list


        ## Optimal -> Prefix Sum Algorithm 
        ## TC = O(n) SC = O(n)

        prefix = np.zeros(n, dtype=np.int32)
        prefix[0] = nums[0]

        for i in range(1, n):
            prefix[i] = prefix[i-1] + nums[i]
        
        return prefix.tolist()
