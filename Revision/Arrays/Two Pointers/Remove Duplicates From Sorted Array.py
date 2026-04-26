from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)

        ## Brute:
        ## TC = O(n2) SC = O(n)

        # answer = []
        # for i in range(n):
        #     if nums[i] not in answer:
        #         answer.append(nums[i])
        
        # for i in range(len(answer)):
        #     nums[i] = answer[i]
        # return len(answer)

        ## Optimal
        ## TC = O(n) SC = O(1)

        left = 0
        right = 1
        while right < n:
            if nums[left] != nums[right]:
                left += 1
                nums[left] = nums[right]
            right += 1
        return left + 1
