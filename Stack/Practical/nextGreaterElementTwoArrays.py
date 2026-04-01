class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        n = len(nums1)
        m = len(nums2)


        ## Brute
        ## TC = O(n) * O(m) 
        ## [O(m) for nums2.index()]
        ## SC = O(n)

        # ans = []
        # for i in range(n):
        #     try:
        #         index = nums2.index(nums1[i])
        #         for j in range(index, m):
        #             hasNGE = False
        #             if nums2[j] > nums2[index]:
        #                 ans.append(nums2[j])
        #                 hasNGE = True
        #                 break
        #         if not hasNGE:
        #             ans.append(-1)
        #     except Exception as e:
        #         continue
        # return ans


        ## Optimal
        ## TC = O(m) + O(n)
        ## SC = O(m) + O(n)

        nge = {}
        stack = []

        for i in range(m-1, -1, -1):
            while len(stack) != 0 and stack[-1] < nums2[i]:
                stack.pop(-1)
            if len(stack) != 0:
                nge.update({ nums2[i] : stack[-1] })
            else:
                nge.update({ nums2[i] : -1 })
            stack.append(nums2[i])

        answer = []
        for i in range(n):
            answer.append(nge[nums1[i]])

        return answer


