class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        ## Brute Force: O(n)
        # for i in range(n):
        #     x = x*x

        ## Optimal Solution (Binary Exponentiation)
        ## O(logn)

        if n == 0:
            return 1
        elif n == 1 or x == 1:
            return x
        elif x == 0:
            return 0
        

        binaryForm = n
        answer = 1

        if n < 0:
            binaryForm = -1 * binaryForm
            x = 1/x

        while binaryForm > 0:
            if binaryForm % 2 == 1:
                answer = answer * x
            x = x * x
        
            binaryForm /= 2
        return answer
        