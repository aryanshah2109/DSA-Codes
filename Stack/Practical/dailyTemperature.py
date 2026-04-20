class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        
        n = len(temperatures)

        ## Brute
        ## TC = O(n2) SC = O(n)
        # answer = []
        # for i in range(n):
        #     hasHigher = False
        #     for j in range(i+1,n):
        #         if temperatures[i] < temperatures[j]:
        #             answer.append(j-i)
        #             hasHigher = True
        #             break
        #     if not hasHigher:
        #         answer.append(0)
        # return answer

        ## Optimal
        ## TC = O(n) SC = O(2n)
        ## Basically, find the next greatest element. if doesnt exist, give 0
        nge = [0] * n
        stack = []
        for i in range(n-1, -1 ,-1):
            while len(stack) != 0 and temperatures[stack[-1]] <= temperatures[i]:
                stack.pop(-1)
            if len(stack) != 0:
                nge[i] = stack[-1] - i
            stack.append(i)
        return nge
            

        