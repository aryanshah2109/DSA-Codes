class Solution(object):
    def getSubsets(self, nums, answer, curr_subset, idx, n):
        
        if idx == n:
            answer.append(curr_subset[:])
            return
        
        # include element
        curr_subset.append(nums[idx])
        self.getSubsets(nums, answer, curr_subset, idx+1, n)

        # backtrack
        curr_subset.pop(-1)

        # exclude element        
        self.getSubsets(nums, answer, curr_subset, idx+1, n)

        return answer


    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ## TC = O(n) * O(2^n)
        ## SC = O(n) * O(2^n)

        all_subsets = self.getSubsets(nums, [], [], 0, len(nums))
        return all_subsets

        