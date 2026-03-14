class MyStack(object):

    def __init__(self):
        self.queue1 = []
        self.queue2 = []
        
    def push(self, x):
        """
        :type x: int
        :rtype: None
        """

        # 1. Append new element to queue 2
        self.queue2.append(x)
        
        # 2. Copy all existing elements of queue 1 into queue 2
        while self.queue1:
            self.queue2.append(self.queue1.pop(0))
        
        # 3. Re push all elements from queue 2 to queue 1
        self.queue1, self.queue2 = self.queue2, self.queue1
        

    def pop(self):
        """
        :rtype: int
        """
        return self.queue1.pop(0)


    def top(self):
        """
        :rtype: int
        """
        return self.queue1[0]
        

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.queue1) == 0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()