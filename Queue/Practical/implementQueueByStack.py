class MyQueue(object):

    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        # Transfer existing elements of s1 to s2
        while self.s1:
            element = self.s1.pop(-1)
            self.s2.append(element)
                
        # Add new element to s1
        self.s1.append(x)

        # Transfer existing elements of s2 to s1
        while self.s2:
            element = self.s2.pop(-1)
            self.s1.append(element)


    def pop(self):
        """
        :rtype: int
        """
        return self.s1.pop(-1)

    def peek(self):
        """
        :rtype: int
        """
        return self.s1[-1]
        

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.s1) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()