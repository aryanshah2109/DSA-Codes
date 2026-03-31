class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        ## TC = O(n) SC = O(n)
        
        # Basically calculate next greatest element
        n = len(temperatures)

        next_warmer_temp = [0] * n
        stack = []

        for i in range(n-1, -1, -1):
            # pop out temperatures which are smaller or equal than current temp
            while len(stack) != 0 and temperatures[stack[-1]] <= temperatures[i]:
                stack.pop(-1)

            # If any element remains in stack, top element is your next greatest for current
            if len(stack) != 0:
                next_warmer_temp[i] = stack[-1] - i
            
            # append indices of next greatest in stack
            stack.append(i)

        return next_warmer_temp
