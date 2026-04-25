class Solution(object):
    def getPrefixMax(self, height):
        
        n = len(height)
        prefix = [0] * n
        prefix[0] = height[0]

        for i in range(1,n):
            prefix[i] = max(prefix[i-1],height[i])

        return prefix
    
    def getSuffixMax(self, height):

        n = len(height)
        suffix = [0] * n
        suffix[n-1] = height[n-1]
        
        for i in range(n-2, -1, -1):
            suffix[i] = max(suffix[i+1], height[i])
        
        return suffix

    
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)

        ## Brute
        ## TC = O(n) SC = O(n)
        # prefix = self.getPrefixMax(height)
        # suffix = self.getSuffixMax(height)
        # totalWater = 0

        # for i in range(n):
        #     left = prefix[i]
        #     right = suffix[i]
        #     if height[i] < left and height[i] < right:
        #         currentWater = min(left, right) - height[i]
        #         totalWater += currentWater
        # return totalWater

        ## Optimal
        ## 2 pointer approach
        ## TC = O(n) SC = O(1)

        left = 0
        right = n-1

        leftMax = 0
        rightMax = 0

        total = 0

        while left < right:
            leftMax = max(leftMax, height[left])
            rightMax = max(rightMax, height[right])

            if leftMax < rightMax:
                total += leftMax - height[left]
                left += 1
                
            else:
                total += rightMax - height[right]
                right -= 1
        
        return total

