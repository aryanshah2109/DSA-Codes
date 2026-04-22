"""
Steps:
    1) Reverse given infix
    2) If any opening brackets, convert to closing brackets and vice versa
    3) Convert result to postfix
    4) Reverse result of postfix and return
"""

def getPriority(char: str):
    if char == "+" or char == "-":
        return 1
    elif char == "*" or char == "/":
        return 2
    elif char == "^":
        return 3
    else:
        return -1

def infixPostfix(s: str) -> str:
    n = len(s)
    stack = []
    postfix = ""

    for char in s:

        if (
            (char >= "A" and char <= "Z") or
            (char >= "a" and char <= "z") or
            (char >= "0" and char <= "9")
        ):
            postfix = postfix + char

        elif char == "(":
            stack.append(char)
        
        elif char == ")":
            while len(stack) != 0 and stack[-1] != "(":
                postfix += stack.pop(-1)
            stack.pop(-1) # Remove "(" too
        
        else:
            if char == "^":
                while len(stack) != 0 and getPriority(char) <= getPriority(stack[-1]):
                    postfix += stack.pop(-1)
                stack.append(char)
            else:
                while len(stack) != 0 and getPriority(char) < getPriority(stack[-1]):
                    postfix += stack.pop(-1)
                stack.append(char)
    
    while len(stack) != 0:  # Empty stack
        postfix += stack.pop(-1)
    
    return postfix


def reverseStr(s: str) -> str:
    reverse = ""
    for char in s:
        reverse = char + reverse
    
    return reverse

def infixPrefix(s: str) -> str:

    reverse = reverseStr(s)

    # swap paranthesis
    reverse = reverse.replace("(", "#")
    reverse = reverse.replace(")", "(")
    reverse = reverse.replace("#", ")")

    postfix = infixPostfix(reverse)

    prefix = reverseStr(postfix)

    return prefix

infix = input("Enter infix expression: ")
prefix = infixPrefix(infix)
print(f"Prefix expression: {prefix}")

