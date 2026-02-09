from typing import List
import numpy as np
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        n = len(nums)

        ## Brute
        ## TC = O(n2) SC = O(1)
        # product_array = []

        # for i in range(n):
        #     product = 1
        #     for j in range(n):
        #         if i != j:
        #             product *= nums[j]
        #     product_array.append(product)
        # return product_array

        ## Better
        ## TC = O(n) SC = O(n)
        ## Calculate prefix and suffix products of each element and multiple prefix and suffix
        ## of that index

        # prefix = [1] * n
        # suffix = [1] * n

        # for i in range(1,n):
        #     prefix[i] = prefix[i-1] * nums[i-1]

        # for i in range(n-2, -1, -1):
        #     suffix[i] = suffix[i+1] * nums[i+1] 

        # for i in range(n):
        #     nums[i] = prefix[i] * suffix[i]
        
        # return nums


        ## Optimal
        ## TC = O(n) SC = O(1)

        ans = [1] * n

        for i in range(1,n):
            ans[i] = ans[i-1] * nums[i-1]
        
        suffix = 1
        for i in range(n-2, -1, -1):
            suffix = suffix * nums[i+1]
            ans[i] *= suffix
        
        return ans
