class StockSpanner(object):

    def __init__(self):
        # self.elements = []
        self.stack = []     # Stores tuple - (value, index)
        self.current_index_num_elements = -1        # Stores index of current element

    def next(self, price):
        """
        :type price: int
        :rtype: int
        """
        
        ## Brute: For every next call, traverse back and find out how many elements
        ## are less than or equal to new element

        ## TC = O(n2) SC = O(n) n = number of next calls

        # self.elements.append(price)
        # n = len(self.elements)
        # count = 0
        # for i in range(n-1, -1, -1):
        #     if self.elements[i] <= price:
        #         count += 1
        #     else:
        #         break
        # return count


        ## Optimal: find previous greater element. if exists, span = difference in index. if doesnt
        ## exist, span = index + 1

        ## For n next calls, TC = O(2n) SC = O(n)

        self.current_index_num_elements += 1

        while len(self.stack) != 0 and self.stack[-1][0] <= price:
            self.stack.pop(-1)
            
        if len(self.stack) == 0:
            span = self.current_index_num_elements + 1
            
        else:
            span = self.current_index_num_elements - self.stack[-1][1]

        self.stack.append((price, self.current_index_num_elements))

        return span


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)