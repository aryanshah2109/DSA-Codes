class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None
    
    def addStart(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            node.next = node
            return
        curr = self.head
        while curr.next != self.head:
            curr = curr.next
        curr.next = node
        node.next = self.head
        self.head = node
    
    def addEnd(self, data):
        node = Node(data)
        if self.head is None:
            return self.addStart(data)
        curr = self.head
        while curr.next != self.head:
            curr = curr.next
        curr.next = node
        node.next = self.head
    
    def deleteStart(self):  
        if self.head is None:
            return 
        if self.head.next == self.head: # Single Node
            self.head = None
            return data
        data = self.head.data
        curr = self.head
        while curr.next != self.head:
            curr = curr.next
        curr.next = self.head.next
        self.head = self.head.next
        return data
        
    
    def deleteEnd(self):
        if self.head is None:
            return
        curr = self.head
        while curr.next.next != self.head:
            curr = curr.next
        data = curr.next.data
        curr.next = self.head
        return data
        
    
    def print(self):
        if self.head is None:
            return -1
        print("\n")
        curr = self.head
        while True:
            print(curr.data, end=" -> ")
            curr = curr.next
            if curr == self.head:
                print("\n")
                break
        
cll = CircularLinkedList()

for i in range(10, 0, -1):
    cll.addStart(i)
    
for i in range(11, 21):
    cll.addEnd(i)

cll.print()
        
print(cll.deleteStart())        
print(cll.deleteStart())        

cll.print()

print(cll.deleteEnd())                
print(cll.deleteEnd())                        
        
cll.print()