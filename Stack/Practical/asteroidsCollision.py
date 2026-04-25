class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        # TC = O(2n) SC = O(n)

        n = len(asteroids)

        stack = []

        for i in range(n):

            if asteroids[i] > 0:
                
                stack.append(asteroids[i])
                continue

            else:

                while len(stack) > 0 and stack[-1] > 0 and -asteroids[i] > stack[-1]:
                    stack.pop(-1)
                    
                if len(stack) > 0 and stack[-1] == -asteroids[i]:
                    stack.pop(-1)

                elif len(stack) == 0 or stack[-1] < 0:
                    stack.append(asteroids[i])

        return stack