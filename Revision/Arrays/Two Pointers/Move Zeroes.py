class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)

        ## Brute
        ## TC = O(n) SC = O(n)

        # temp = []
        # for i in range(n):
        #     if nums[i] != 0:
        #         temp.append(nums[i])

        
        # for i in range(n):
        #     if i < len(temp):
        #         nums[i] = temp[i]
        #     else:
        #         nums[i] = 0
            
        
        ## Optimal
        ## TC = O(n) SC = O(1)

        # Find first zero
        j = -1
        for i in range(n):
            if nums[i] == 0:
                j = i
                break

        if j == -1:      # No zero found
            return

        for i in range(j+1, n):
            if nums[i] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1
        
        
