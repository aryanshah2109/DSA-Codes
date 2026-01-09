class Node:
    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_start(self, data):
        node = Node(data)

        if self.head is None:
            self.head = node
            print(f"\n{data} inserted at start")
            return
    
        self.head.prev = node
        node.next = self.head
        self.head = node
        print(f"\n{data} inserted at start")

    def reverse_dll(self):
        if self.head is None:
            print("\nEmpty linked list")
            return
        
        temp = self.head
        prev = None

        while temp is not None:
            prev = temp.prev
            temp.prev = temp.next
            temp.next = prev
            temp = temp.prev
        
        self.head = prev.prev
        print("\nReversed doubly linked list.")
        return

    def print_ll(self):
        if self.head is None:
            print(f"\nEmpty Linked List")
            return
        
        curr = self.head

        print("\nLinked List: ",end="")
        
        while curr is not None:
            print(f" {curr.data} ", end="<=>")
            curr = curr.next
        
        print("\n")
        

def main():
    doublyll = DoublyLinkedList()

    doublyll.print_ll()

    doublyll.insert_start(20)
    doublyll.insert_start(15)
    doublyll.insert_start(10)
    doublyll.insert_start(5)

    
    doublyll.print_ll()

    doublyll.reverse_dll()

    doublyll.print_ll()

    
if __name__ == "__main__":
    main()