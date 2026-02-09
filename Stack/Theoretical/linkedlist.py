class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_start(self, data):
        node = Node(data)

        if self.head is None:
            self.head = node
            return

        node.next = self.head
        self.head = node

    def insert_end(self, data):
        node = Node(data)

        if self.head is None:
            self.insert_start(data)
            return
        
        curr = self.head
        while curr.next:
            curr = curr.next
        
        curr.next = node

    def delete_start(self):
        if self.head is None:
            raise ValueError("Cannot delete from empty Linked List")

        curr = self.head
        data = curr.data
        self.head = curr.next
        curr.next = None
        print(data)


    def delete_end(self):
        if self.head is  None:
            raise ValueError("Cannot delete from an empty Linked List")
        
        curr = self.head
        while curr.next.next:
            curr = curr.next
        
        data = curr.next.data
        curr.next = None
        print(data)

    def print_ll(self):
        if self.head is None:
            raise ValueError("Empty Linked List.")
        
        curr = self.head

        while curr:
            print(f"{curr.data} -> ", end=" ")
            curr = curr.next

class Stack:
    MAX_SIZE = 10
    def __init__(self):
        self.top = -1
        self.linked = LinkedList()

    def push(self, data):
        if self.top == Stack.MAX_SIZE - 1:
            raise ValueError("Stack Overflow.")
        
        self.top += 1
        self.linked.insert_start(data)

    def pop(self):
        if self.top == -1:
            raise ValueError("Stack Underflow. Cannot pop from empty stack")
        
        print("Popped element: ", end=" ")
        self.linked.delete_start()
        
    
    def display(self):
        if self.top == -1:
            raise ValueError("Stack Underflow. No elements to display")
        
        self.linked.print_ll()

    def top_element(self):
        if self.top == -1:
            raise ValueError("Stack Underflow. No top element in stack")
    
        return self.linked.head.data


st = Stack()

try:
    # st.pop()
    # st.top_element()
    # st.display()

    st.push(1)
    st.push(2)
    st.push(3)
    st.push(4)
    st.push(5)
    st.push(10)
    st.push(15)
    st.push(20)
    st.push(25)
    st.push(30)
    # st.push(35)
    # st.push(40)

    st.display()

    print("\nDeleting elements: ")
    st.pop()
    st.pop()
    print("")
    st.display()


    print(f"\nTop element: {st.top_element()}")
    



except Exception as e:
    print(e)
    
        
        
        

