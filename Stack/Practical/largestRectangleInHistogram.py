class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        n = len(heights)

        ## Brute
        ## TC = O(n2) SC = O(1)
        # max_area = 0
        # for i in range(n):
        #     current_area = 0
        #     min_height = heights[i]
        #     for j in range(i, n):
        #         min_height = min(min_height, heights[j])
        #         width = j-i+1
        #         current_area = min_height * width
        #         max_area = max(current_area, max_area)
        # return max_area

        ## Optimal
        ## TC = O(n) SC = O(4n)
        ## Find next smallest and previous smallest element. 
        pse = [-1] * n
        stack = []
        for i in range(n):
            while len(stack) != 0 and heights[stack[-1]] >= heights[i]:
                stack.pop(-1)
            if len(stack) != 0:
                pse[i] = stack[-1]
            stack.append(i)
        
        nse = [n] * n
        stack = []
        for i in range(n-1, -1, -1):
            while len(stack) != 0 and heights[stack[-1]] >= heights[i]:
                stack.pop(-1)
            if len(stack) != 0:
                nse[i] = stack[-1]
            stack.append(i)
        
        ## Width will be nse - pse - 1
        max_area = 0
        for i in range(n):
            width = nse[i] - pse[i] - 1
            curr_area = heights[i] * width
            max_area = max(max_area, curr_area)
        return max_area
