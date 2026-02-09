class Stack:
    MAX_SIZE = 10
    def __init__(self):
        self.top = -1
        self.stack = []

    
    def push(self, data):
        if self.top == Stack.MAX_SIZE - 1:
            raise ValueError(f"Stack Overflow while inserting {data}")
        
        self.top += 1
        self.stack.append(data)

    def pop(self):
        if self.top == -1:
            raise ValueError("Stack Underflow. Cannot pop from empty stack")
        
        data = self.stack[-1]
        self.top -= 1
        self.stack.pop()
        return data
    
    def top_element(self):
        if self.top == -1:
            raise ValueError("Stack Underflow. No top element")
        
        return self.stack[self.top]
    
    def display(self):
        if self.top == -1:
            raise ValueError("Stack Underflow. No elements to display")

        print("Stack: ")
        temp = self.top
        while temp != -1:
            print(self.stack[temp])
            temp -= 1


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
    print(st.pop())
    print(st.pop())
    print("")
    st.display()

    print("\nTop element: ")
    print(st.top_element())



except Exception as e:
    print(e)
    