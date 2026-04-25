class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        ## TC = O(n) SC = O(n)
        
        stack = []

        for operation in operations:

            if operation == "+":
                
                top_element = stack[-1]
                second_top_element = stack[-2]

                stack.append(top_element + second_top_element)

            elif operation == "C":
                stack.pop(-1)
            
            elif operation == "D":
                stack.append(stack[-1] * 2)

            else:
                stack.append(int(operation))

        score_sum = 0
        
        for i in range(len(stack)):
            score_sum += stack[i]

        return score_sum