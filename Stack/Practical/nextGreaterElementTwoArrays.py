class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        ## Brute: TC = O(n2) SC = O(n)
        ## For each element in nums1, first find its index in nums2
        ## Then find its next greatest element by 2 loops

        ## Optimal
        ## TC = O(n) SC = O(2n)
        
        # First find nge of all elements in nums2
        nge = {}
        stack = []
        for i in range(len(nums2) - 1, -1, -1):
            while len(stack) > 0 and stack[-1] <= nums2[i]:
                stack.pop(-1)

            if len(stack) != 0:
                nge.update({nums2[i] : stack[-1]})
            else:
                nge.update({nums2[i]: -1})
            
            stack.append(nums2[i])
        
        # Then for every index in nums1, find its appropriate nge
        ans = []
        for i in range(len(nums1)):
            ans.append(nge[nums1[i]])

        return ans
        



