class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        
        n = len(nums)

        ## Brute
        ## TC = O(n-k)*O(k) SC = O(n-k)
        # max_window = []
        # for i in range(n-k+1):
        #     curr_max = nums[i]
        #     for j in range(i, i+k):
        #         curr_max = max(curr_max, nums[j])
        #     max_window.append(curr_max)
        # return max_window

        ## Optimal
        ## TC = O(n) + O(k) 
        ## SC = O(k)

        deque = []
        ans = []

        for i in range(n):

            # removes index if you have moved window and index not in new window
            if len(deque) != 0 and deque[0] == i - k:    
                deque.pop(0)

            # remove any elements from deque if current element larger than deque back element
            while len(deque) != 0 and nums[i] > nums[deque[-1]]:
                deque.pop(-1)
            
            # add current element into back of deque
            deque.append(i)

            # add max element into answer
            if i >= k-1:
                ans.append(nums[deque[0]])

        return ans
