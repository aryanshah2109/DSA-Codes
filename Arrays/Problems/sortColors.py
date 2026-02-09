from typing import List
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)

        ## Brute
        ## TC = O(n2) SC = O(1)
        ### Sort the array by bubble sort or any other sorting algorithm
        # for i in range(n-1):
        #     for j in range(n-1-i):
        #         if nums[j] > nums[j+1]:
        #             temp = nums[j]
        #             nums[j] = nums[j+1]
        #             nums[j+1] = temp
        # return nums

        ## Better
        ## TC = O(n) SC = O(1)
        # no0 = 0
        # no1 = 0
        # no2 = 0
        # for i in range(n):
        #     if nums[i] == 0:
        #         no0 += 1
        #     elif nums[i] == 1:
        #         no1 += 1
        #     else:
        #         no2 += 1
        
        # for i in range(n):
        #     if i < no0:
        #         nums[i] = 0
        #     elif i < no0 + no1:
        #         nums[i] = 1
        #     else:
        #         nums[i] = 2

        # return nums

        ## Optimal
        ## TC = O() SC = O()
        ### DUTCH FLAG ALGORITHM
        low = 0
        mid = 0
        high = n-1

        while mid <= high:
            if nums[mid] == 0:
                temp = nums[low]
                nums[low] = nums[mid]
                nums[mid] = temp

                mid += 1
                low += 1

            elif nums[mid] == 1:
                mid += 1

            else:
                temp = nums[mid]
                nums[mid] = nums[high]
                nums[high] = temp
                high -= 1

        return nums

