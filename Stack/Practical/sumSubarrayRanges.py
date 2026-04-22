class Solution(object):
    def findPSE(self, nums):
        n = len(nums)
        pse = [-1] * n
        stack = []
        for i in range(n):
            while len(stack) != 0 and nums[stack[-1]] > nums[i]:
                stack.pop(-1)
            if len(stack) != 0:
                pse[i] = stack[-1]
            stack.append(i)
        return pse
    
    def findNSE(self, nums):
        n = len(nums)
        nse = [n] * n
        stack = []
        for i in range(n-1, -1,-1):
            while len(stack) != 0 and nums[stack[-1]] >= nums[i]:
                stack.pop(-1)
            if len(stack) != 0:
                nse[i] = stack[-1]
            stack.append(i)
        return nse

    def findPGE(self, nums):
        n = len(nums)
        pge = [-1] * n
        stack = []
        for i in range(n):
            while len(stack) != 0 and nums[stack[-1]] < nums[i]:
                stack.pop(-1)
            if len(stack) != 0:
                pge[i] = stack[-1]
            stack.append(i)
        return pge

    def findNGE(self, nums):
        n = len(nums)
        nge = [n] * n
        stack = []
        for i in range(n-1, -1, -1):
            while len(stack) != 0 and nums[stack[-1]] <= nums[i]:
                stack.pop(-1)
            if len(stack) != 0:
                nge[i] = stack[-1]
            stack.append(i)
        return nge

    def subArrayRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)

        ## Brute
        ## TC = O(n2) SC = O(1)
        # total = 0
        # for i in range(n):
        #     largest = nums[i]
        #     smallest = nums[i]
        #     for j in range(i, n):
        #         if nums[j] > largest:
        #             largest = nums[j]
        #         if nums[j] < smallest:
        #             smallest = nums[j]
        #         total += (largest - smallest)
        # return total

        ## Optimal
        ## For minimum, use sum of subarray minimums problem method
        ## For maximum, use sum of subarray minimums problem method but find pge and nge instead
        ## of pse and nse

        ## TC = O(n) SC = O(n)

        # find all monotonic stacks
    
        pse = self.findPSE(nums)
        nse = self.findNSE(nums)
        pge = self.findPGE(nums)
        nge = self.findNGE(nums)

        total_min = 0
        total_max = 0

        for i in range(n):

            # Minimum
            left = i - pse[i]
            right = nse[i] - i
            individual_min = left * right * nums[i]
            total_min += individual_min
        
            # Maximum
            left = i - pge[i]
            right = nge[i] - i
            individual_max = left * right * nums[i]
            total_max += individual_max

        return total_max - total_min
        




