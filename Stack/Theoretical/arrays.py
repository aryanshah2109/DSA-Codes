## TC = O(1) SC = O(max_size) ~ O(1)
## Disadvantage of using stack as array: Must pass size. Cannot have dynamic size

class Stack:
    def __init__(self, max_size: int):
        self.stack = []
        self.top = -1
        self.max_size = max_size
    
    def push(self, element: int):
        if self.top == self.max_size - 1:
            print("Stack Overflow")
            return
        self.top += 1
        self.stack.append(element)
        
    def pop(self):
        if self.top == -1:
            print("Stack Underflow")
            return -1
        data = self.stack[self.top]
        self.stack.pop()
        self.top -= 1
        return data
    
    def print(self):
        if self.top == -1:
            print("Stack Underflow")
            return
        temp = self.top
        print("\nStack elements: \n")
        while temp != -1:
            print(self.stack[temp])
            temp -= 1
    
    def top_element(self):
        if self.top == -1:
            print("Stack underflow")
            return -1
        return self.stack[self.top]
    
s = Stack(10)

for i in range(1, 11):
    s.push(i)

s.print()

print("\n")

print("Popping elements: \n")
for i in range(3):
    print(s.pop())

s.print()

print("\nTop element: ")
print(s.top_element())