class Solution(object):
    def brute(self, nums, storage, marker, n, answer):
        if len(storage) == n:
            answer.append(storage[:])
            return

        for i in range(len(marker)):
            if not marker[i]:
                marker[i] = True
                storage.append(nums[i])
                self.brute(nums, storage, marker, n, answer)
                
                storage.pop(-1)
                marker[i] = False
    
        return answer

    def optimal(self, nums, answer, idx):
        if idx == len(nums):
            answer.append(nums[:])
            return 

        for i in range(idx, len(nums)):

            nums[i], nums[idx] = nums[idx], nums[i]     # idx place = ith element
            self.optimal(nums, answer, idx + 1)
            nums[i], nums[idx] = nums[idx], nums[i]     # backtrack

        return answer

    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        ## Brute ( Using extra space)
        ## TC = O(n! * n) 
        ## SC = O(n) recursion + O(n) marker + output

        # marker = [False] * len(nums)
        # answer = self.brute(nums, [], marker, len(nums), [])
        # return answer

        ## Optimal
        ## TC = O(n! * n)
        ## SC = O(n) recursion + O(n) answer array
        answer = self.optimal(nums, [], 0)
        return answer