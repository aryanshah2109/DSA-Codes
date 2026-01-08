class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_start(self, data):
        node = Node(data)

        node.next = self.head

        self.head = node

        print(f"Successfully added {data} at start")
    
    def insert_end(self, data):
        node = Node(data)

        if self.head is None:
            self.insert_start(data)
            print(f"Successfully added {data} at end")
            return

        current = self.head

        while current.next:
            current = current.next

        current.next = node

        print(f"Successfully added {data} at end")
    
    def insert_k(self, data, k):

        if k == 0:
            self.insert_start(data)
            print(f"Successfully added {data} at index {k}")
            return
        
        node = Node(data)
        
        current = self.head

        for i in range(k-1):
            current = current.next
        
        node.next = current.next
        current.next = node

        print(f"Successfully added {data} at index {k}")      
    
    def search_val(self, val):
        if self.head is None:
            print(f"\nEmpty Linked List. Could not search {val}")
            return
        
        curr = self.head
        count = 0

        while curr is not None:
            count += 1
            if curr.data == val:
                print(f"\nElement {val} found at position {count}")
                return
            curr = curr.next    
        print(f"\nElement {val} not present in the linked list")

    def delete_val(self, val):
        if self.head is None:
            print(f"Empty Linked List. Could not delete {val}")
            return
        
        if self.head.data == val:
            self.delete_start()
            return
        
        curr = self.head

        while curr.next is not None:
            if curr.next.data == val:
                curr.next = curr.next.next
                print(f"\nElement {val} deleted from linked list")
                return
            curr = curr.next
        
        print(f"\nElement {val} not found in linked list")

    def delete_start(self):
        if self.head is None:
            print("No node present to delete!")
            return

        data  = self.head.data

        self.head = self.head.next

        print(f"Node at start with data {data} deleted!")

    def delete_end(self):
        if self.head is None:
            print("No node left to delete\n")
            return
        
        current = self.head

        while current.next.next is not None:
            current = current.next

        data = current.next.data
        current.next = None

        print(f"Node at end with data {data} deleted!")

    def delete_k(self, k):
        if self.head is None:
            print("\nNo node left to delete\n")
            return
        
        current = self.head

        for i in range(k-1):
            current = current.next

        data = current.next.data
        current.next = current.next.next

        print(f"Node at end with data {data} deleted!")


    def print_linkedlist(self):

        if self.head is None:
            print("Empty Linked List!\n")
            return

        current = self.head
        print("\nLinked List: ")
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("\n")
        

def main():

    linkedlist = LinkedList()

    linkedlist.print_linkedlist()

    linkedlist.insert_start(5)
    linkedlist.insert_start(4)
    linkedlist.insert_start(3)
    linkedlist.insert_start(2)

    linkedlist.print_linkedlist()

    linkedlist.insert_end(6)
    linkedlist.insert_end(7)
    linkedlist.insert_end(8)

    linkedlist.print_linkedlist()

    linkedlist.insert_k(100, 2)

    linkedlist.print_linkedlist()

    linkedlist.delete_start()

    linkedlist.print_linkedlist()

    linkedlist.delete_end()

    linkedlist.print_linkedlist()

    linkedlist.delete_k(2)

    linkedlist.print_linkedlist()

    linkedlist.search_val(5)
    linkedlist.search_val(7)
    linkedlist.search_val(3)
    linkedlist.search_val(9)

    linkedlist.print_linkedlist()

    linkedlist.delete_val(5)
    linkedlist.print_linkedlist()

    linkedlist.delete_val(7)
    linkedlist.print_linkedlist()

    linkedlist.delete_val(3)
    linkedlist.print_linkedlist()

if __name__ == "__main__":
    main()