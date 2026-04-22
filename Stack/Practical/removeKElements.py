class Solution(object):
    def removeKdigits(self, num, k):
        ## TC = O(3n) + O(k) SC = O(n) + O(n)

        stack = []

        # For each digit, remove only if current value is smaller than previous value
        for digit in num:
            while stack and k > 0 and stack[-1] > digit:
                stack.pop()
                k -= 1
            stack.append(digit)

        # If k still remains, remove from end
        while k > 0:
            stack.pop()
            k -= 1

        # Build result -> convert all stack elements to string
        result = "".join(stack)

        # Remove leading zeros
        result = result.lstrip('0')

        return result if result else "0"