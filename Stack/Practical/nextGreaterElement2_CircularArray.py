class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)


        ## Brute
        ## TC = O(n2) SC = O(n)

        # nge = []
        # for i in range(n):
        #     found = False
        #     for j in range(i+1, n):
        #         if nums[j] > nums[i]:
        #             nge.append(nums[j])
        #             found = True
        #             break
        #     if not found:
        #         circular_found = False
        #         for j in range(0, i):
        #             if nums[j] > nums[i]:
        #                 nge.append(nums[j])
        #                 circular_found = True
        #                 break
        #         if not circular_found:
        #             nge.append(-1)

        # return nge



        ## Optimal: Consider the circular array as 2 same arrays placed side by side
        ## TC = O(n) SC = O(n)

        nge = [-1] * n
        stack = []

        for i in range(2 * n - 1, -1, -1):
            while len(stack) != 0 and stack[-1] <= nums[i%n]:
                stack.pop(-1)
            
            if len(stack) != 0 and i < n:
                nge[i] = stack[-1]
            
            stack.append(nums[i%n])

        return nge
