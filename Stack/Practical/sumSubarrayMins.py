class Solution(object):
    def sumSubarrayMins(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        n = len(arr)
        mod = 10**9 + 7
        
        ## Brute
        ## TC = O(n2) SC = O(1)
        # total = 0
        # for i in range(n):
        #     minimal = arr[i]
        #     for j in range(i, n):
        #         minimal = min(minimal, arr[j])
        #         total = (total + minimal) % mod
        # return int(total)
                    

        ## Optimal
        ## TC = O(n + n + n) ~ O(n)
        ## SC = O(3n) ~ O(n)

        ## Find pse and nse for all elements. Find individual contribution and add them

        # Find pse
        pse = [-1] * n
        stack = []
    
        for i in range(n):

            while len(stack) != 0 and arr[stack[-1]] > arr[i]:
                stack.pop(-1)

            if len(stack) != 0:
                pse[i] = stack[-1]
                
            stack.append(i)
        
        # Find nse
        nse = [n] * n
        stack = []
    
        for i in range(n-1, -1, -1):
            while len(stack) != 0 and arr[stack[-1]] >= arr[i]:
                stack.pop(-1)
            if len(stack) != 0:
                nse[i] = stack[-1]
            stack.append(i)
        
        # find contributions
        total = 0
        for i in range(n):
            left = i - pse[i]
            right = nse[i] - i
            individual_contribution = left * right * arr[i]
            total = (total + individual_contribution) % mod
        
        return total


        