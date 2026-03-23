class Solution(object):
    def sumSubarrayMins(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        n = len(arr)
        mod_val = int(1e9 + 7)

        ## Brute
        ## TC = O(n2) SC = O(1)
        # minimum = float("inf")
        # total_sum = 0
    
        # for i in range(n):
        #     minimum = arr[i]
        #     for j in range(i, n):
        #         minimum = min(minimum, arr[j])
        #         total_sum = (total_sum + minimum) % mod_val 
        # return total_sum

        
        ## Optimal
        

        # previous smaller element
        pse = []
        stack = []
        for i in range(n):
            while len(stack) != 0 and arr[stack[-1]] > arr[i]:
                stack.pop(-1)
            if len(stack) == 0:
                pse.append(-1)
            else:
                pse.append(stack[-1])
            stack.append(i)
        
        # next smallest element
        nse = [n] * n
        stack = []
        for i in range(n-1, -1, -1):
            while len(stack) != 0 and arr[stack[-1]] >= arr[i]:
                stack.pop(-1)
    
            if len(stack) != 0:
                nse[i] = stack[-1]
    
            stack.append(i)

        total = 0

        for i in range(n):
            left = i - pse[i]
            right = nse[i] - i
            total = (total + (left * right * arr[i]) %  mod_val) % mod_val
        
        return total