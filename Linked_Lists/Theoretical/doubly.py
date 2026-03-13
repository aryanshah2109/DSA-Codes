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

    def insert_end(self,data):
        node = Node(data)

        if self.head is None:
            self.head = node
            print(f"\nNo element in linked list so inserted {data} at start")
            return

        curr = self.head

        while curr.next is not None:
            curr = curr.next

        curr.next = node
        node.prev = curr

        print(f"\n{data} inserted at end")

    def delete_start(self):
        if self.head is None:
            print(f"\nEmpty linked list. Cannot delete")
            return
        
        data = self.head.data
        self.head = self.head.next
        self.head.prev = None
        print(f"\n{data} deleted from start of linked list")

    def delete_end(self):
        if self.head is None:
            print(f"\nEmpty linked list. Cannot delete")
            return
        
        curr = self.head

        while curr.next.next is not None:
            curr = curr.next
        
        data = curr.next.data
        curr.next.prev = None
        curr.next = None
        print(f"\n{data} deleted from end of linked list")



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

    doublyll.insert_end(25)
    doublyll.insert_end(30)
    doublyll.insert_end(35)

    doublyll.print_ll()

    doublyll.delete_start()
    doublyll.delete_start()

    doublyll.print_ll()

    doublyll.delete_end()
    doublyll.delete_end()

    doublyll.print_ll()


if __name__ == "__main__":
    main()