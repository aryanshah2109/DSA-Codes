class MinStack(object):

    def __init__(self):
        self.s = []
        self.top_idx = -1
        self.min = float("inf")

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        if self.top_idx == -1:
            self.s.append(val)
            self.min = val

        elif val < self.min:
            # Store modified value into stack
            newVal = 2 * val - self.min
            self.s.append(newVal)

            # Store new minimum 
            self.min = val

        else:
            self.s.append(val)            

        # Update top idx
        self.top_idx += 1


    def pop(self):
        """
        :rtype: None
        """
        if self.top_idx == -1:
            return 

        val = self.s.pop(self.top_idx)
        self.top_idx -= 1

        if val < self.min:  
            original = self.min
            self.min = 2 * self.min - val
            return original

        return val
        

    def top(self):
        """
        :rtype: int
        """
        if self.top_idx == -1:
            return
        val = self.s[self.top_idx]
        if val < self.min:
            return self.min
        return val


    def getMin(self):
        """
        :rtype: int
        """
        return self.min


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()