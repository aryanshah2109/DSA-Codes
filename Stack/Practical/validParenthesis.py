class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for char in s:
            if char in ["[", "(", "{"]:
                stack.append(char)
            else:
                if not stack: # First character is closing bracket
                    return False

                top = stack[-1]
                if (char == "]" and top == "[") or (char == ")" and top == "(") or (char == "}" and top == "{"):
                    stack.pop()
                else:
                    return False
        
        return len(stack) == 0 # If stack contains only opening brackets
                