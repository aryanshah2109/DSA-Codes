class Solution(object):
    def largestRectangleInHistogram(self, arr):

        n = len(arr)

        # find previous smallest element
        pse = [-1] * n
        stack = []
        for i in range(n):
            while len(stack) != 0 and arr[stack[-1]] >= arr[i]:
                stack.pop(-1)
            if len(stack) != 0:
                pse[i] = stack[-1]
            stack.append(i)

        # find next smallest element
        nse = [n] * n
        stack = []
        for i in range(n-1, -1, -1):
            while len(stack) != 0 and arr[stack[-1]] >= arr[i]:
                stack.pop(-1)
            if len(stack) != 0:
                nse[i] = stack[-1]
            stack.append(i)

        # calculate max area
        maxArea = 0
        for i in range(n):
            width = nse[i] - pse[i] - 1
            currentArea = width * arr[i]
            maxArea = max(currentArea, maxArea)
        return maxArea


    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """

        ## TC = O(m*n + m*n) ~ O(m*n)
        ## SC = O(m*n) + O(3m) ~ O(m*n)

        n = len(matrix)
        m = len(matrix[0])

        prefixSum = [[0] * m for _ in range(n)]
        maxSum = 0

        # create column wise prefix sum matrix
        for i in range(m):
            for j in range(n):
                if matrix[j][i] != "0":
                    if j != 0:
                        prefixSum[j][i] = prefixSum[j-1][i] + 1
                    else:       ## first row
                        prefixSum[j][i] = 1
                else:
                    prefixSum[j][i] = 0
                    
        # for each row of prefix sum, calculate maxArea by largest rectangle in histogram method
        maxArea = 0
        for i in range(n):
            rowArea = self.largestRectangleInHistogram(prefixSum[i])
            maxArea = max(maxArea, rowArea)
        return maxArea


                


