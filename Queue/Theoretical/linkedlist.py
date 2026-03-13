## Advantage: No need to pass max size like arrays
## How to run? from root, python -m Queue.Theoretical.linkedlist

from Linked_Lists.Theoretical.singly import LinkedList, Node

class Queue:
    def __init__(self):
        self.queue = LinkedList()
        self.front = None
        self.last = None

    def push(self, element: int):
        new_node = Node(element)
        if self.last is None:
            self.front = new_node
            self.last = new_node
            return
        
        self.last.next = new_node
        self.last = self.last.next

    def pop(self):
        if self.front is None:
            return 
        data = self.front.data
        self.front = self.front.next

        if self.front is None:
            self.last = None

        return data
    
    def display(self):
        if self.front is None:
            return 
        temp = self.front

        print("\nQueue: ")
        while temp:
            print(temp.data, end=" ")
            temp = temp.next

    def top(self):
        if self.front is None:
            return

        return self.front.data

q = Queue()


for i in range(1, 11):
    q.push(i)

q.display()

print("\n")

print("Popping elements: ")
for i in range(3):
    print(q.pop())

q.display()

print("\n\nTop element: ")
print(q.top())