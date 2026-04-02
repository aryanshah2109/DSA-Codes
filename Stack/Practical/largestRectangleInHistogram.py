class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        ## TC = O(n) SC = O(3n)

        n = len(heights)

        ## Calculate previous smaller and next smaller element indices
        nse = [n] * n
        stack = []

        for i in range(n-1, -1 ,-1):
            while len(stack) != 0 and heights[stack[-1]] >= heights[i]:
                stack.pop(-1)
            if len(stack) != 0:
                nse[i] = stack[-1]
            stack.append(i)

        pse = [-1] * n
        stack = []

        for i in range(n):
            while len(stack) != 0 and heights[stack[-1]] >= heights[i]:
                stack.pop(-1)
            if len(stack) != 0:
                pse[i] = stack[-1]
            stack.append(i)
                

        max_area = 0

        for i in range(n):
            width = nse[i] - pse[i] -1
            
            current_area = heights[i] * width
            max_area = max(max_area, current_area)
        
        return max_area