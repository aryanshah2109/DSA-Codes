## Advantage: No need to pass max size like arrays
## How to run? from root, python -m Stack.Theoretical.linkedlist

from Linked_Lists.Theoretical.singly import LinkedList, Node

class Stack:
    def __init__(self):
        self.stack = LinkedList()

    def push(self, element: int):
        new_node = Node(element)
        new_node.next = self.stack.head
        self.stack.head = new_node

    def pop(self):
        if self.stack.head is None:
            return
        data = self.stack.head.data
        self.stack.head = self.stack.head.next
        return data
    
    def display(self):
        if self.stack.head is None:
            return
        temp = self.stack.head
        print("\nStack:")
        while temp:
            print(temp.data)
            temp = temp.next

    def top(self):
        if self.stack.head is None:
            return
        return self.stack.head.data
    
s = Stack()

for i in range(1, 11):
    s.push(i)

s.display()

print("\n")

print("Popping elements: \n")
for i in range(3):
    print(s.pop())

s.display()

print("\nTop element: ")
print(s.top())