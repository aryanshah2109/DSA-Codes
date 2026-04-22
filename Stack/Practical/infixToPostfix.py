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
            while len(stack) != 0 and getPriority(char) <= getPriority(stack[-1]):
                postfix += stack.pop(-1)
            stack.append(char)
    
    while len(stack) != 0:  # Empty stack
        postfix += stack.pop(-1)
    
    return postfix

infix = input("Enter infix expression: ")
postfix = infixPostfix(infix)
print(f"Postfix expression: {postfix}")