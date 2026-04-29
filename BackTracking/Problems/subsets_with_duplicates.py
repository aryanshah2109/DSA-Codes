class Solution(object):
    def getAllSubsets(self, nums, answer, curr_subset, idx):

        if idx == len(nums):
            answer.append(curr_subset[:])
            return
        
        # include element
        curr_subset.append(nums[idx])
        self.getAllSubsets(nums, answer, curr_subset, idx+1)

        # backtrack
        curr_subset.pop(-1)

        # exclude element

        # directly go to next unique element and skip all recurring duplicates
        i = idx + 1
        
        while i < len(nums) and nums[i] == nums[i-1]:
            i += 1

        self.getAllSubsets(nums, answer, curr_subset, i)

        return answer

    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        ## TC = O(nlogn) + ( O(n) * O(2^n) ) ~ O(n*2^n)
        ## SC = O(n) * O(2^n)

        # 1. Sort the array to make all duplicates occur together
        nums.sort()

        # 2. get all subsets
        all_subsets = self.getAllSubsets(nums, [], [], 0)

        return all_subsets