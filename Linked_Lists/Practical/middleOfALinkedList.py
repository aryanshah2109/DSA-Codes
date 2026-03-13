# Implement Linked List

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    def addStart(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node
        
    def addEnd(self, data):
        node = Node(data)
        if self.head is None:
            self.addStart(data)
            return
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = node
    
    def deleteStart(self):
        if self.head is None:
            return -1
        data = self.head.data
        self.head = self.head.next
        return data
    
    def deleteEnd(self):
        if self.head is None:
            return -1
        current = self.head
        while current.next.next is not None:
            current = current.next
        data = current.next.data
        current.next = None
        return data
        
    def print(self):
        if self.head is None:
            return
        current = self.head
        while current is not None:
            print(current.data, end=" -> ")
            current = current.next
        print(None)
        
    
    def middleElementBruteForce(self):
        ## TC = O(2n) SC = O(1)
        if self.head is None:
            return -1
        # Calculate size of Linked List
        size = 0
        current = self.head
        while current is not None:
            current = current.next
            size += 1
        element = (size // 2) + 1
        
        current = self.head
        index = 0
        while current is not None:
            index += 1
            if index == element:
                return current.data
            current = current.next
        
    def middleElementSlowFastApproach(self):
        ## TC = O(n) SC = O(1)
        if self.head is None:
            return -1
        slow = self.head
        fast = self.head
        
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            
        return slow.data
    
    
ll = LinkedList()

for i in range(1,11):
    ll.addEnd(i)
        
ll.print()        

print(ll.middleElementBruteForce())

print(ll.middleElementSlowFastApproach())