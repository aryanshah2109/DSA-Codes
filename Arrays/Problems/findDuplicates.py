class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)

        ## Brute
        ## TC = O(n2) SC = O(1)       
        # for i in range(n):
        #     for j in range(i+1, n):
        #         if nums[i] == nums[j]:
        #             return nums[i]

        ## Better
        ## TC = O(n) SC = O(n)
        # hashmap = {}
        # for i in range(n):
        #     if nums[i] in hashmap:
        #         hashmap[nums[i]] += 1
        #     else:
        #         hashmap.update({nums[i]: 1})
        # for key, value in hashmap.items():
        #     if value != 1:
        #         return key

        ## Optimal: Similar to slow fast approach in linked lists
        ## TC = O(n) SC = O(1)

        slow = nums[0]
        fast = nums[0]

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break
            
        slow = nums[0]

        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        
        return slow
