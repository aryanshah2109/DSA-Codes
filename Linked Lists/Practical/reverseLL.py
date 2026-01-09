# Method 1: TC = O(n) SC = O(n)
# Use a stack. traverse from head -> end and while traversing, push elements in stack
# Then retraverse from head -> start and while traversing, pop elements from stack 
# and then replace them with the current data in the Linked list


# Method 2: 

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_end(self, data):
        node = Node(data)

        if self.head is None:
            print(f"\nEmpty linked list. Adding {data} at start")
            self.head = node
            return

        curr = self.head

        while curr.next is not None:
            curr = curr.next

        curr.next = node
        print(f"Successfully inserted {data} to linked list")
        return

    def reverse_ll(self):
        if self.head is None:
            print("\nEmpty Linked List.")
            return
    
        prev = None
        temp = self.head

        while temp is not None:
            front = temp.next
            temp.next = prev
            prev = temp
            temp = front 
        
        self.head = prev        # Updating head to last element
        print("\nReversed Linked List successfully.")


    def print_ll(self):
        if self.head is None:
            print("\nEmpty linked list.")

        curr = self.head

        print("\nLinked List: ")
        while curr is not None:
            print(f"{curr.data}", end=" -> ")
            curr = curr.next
        
ll = LinkedList()

ll.insert_end(5)
ll.insert_end(6)
ll.insert_end(7)
ll.insert_end(8)
ll.insert_end(9)
ll.insert_end(10)

ll.print_ll()

ll.reverse_ll()

ll.print_ll()