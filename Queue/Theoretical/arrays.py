class Queue:
    def __init__(self, max_size: int):
        self.queue = []
        self.max_size = max_size
        self.front = -1
        self.last = -1
    
    def push(self, element: int):
        if self.last == self.max_size - 1:
            print("Queue overflow")
            return
        self.queue.append(element)
        if self.front == -1:
            self.front += 1
        self.last += 1


    def pop(self):
        if self.front > self.last:
            print("Queue underflow")
            return
        data = self.queue[self.front]
        self.front += 1
        if self.front > self.last:
            self.front = self.last = -1
        return data

    def display(self):
        if self.front == -1 or self.front > self.last:
            print("Queue underflow")
            return
        temp = self.front
        print("\nQueue elements: ")
        while temp <= self.last:
            print(self.queue[temp], end=" ")
            temp += 1

    def top(self):
        if self.front > self.last:
            print("Queue underflow")
            return 
        return self.queue[self.front]

q = Queue(10)


for i in range(1, 11):
    q.push(i)

q.display()

print("\n")

print("Popping elements: ")
for i in range(3):
    print(q.pop())

q.display()

print("\nTop element: ")
print(q.top())
