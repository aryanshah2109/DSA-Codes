from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        n = len(height)

        ### Brute
        ### TC = O(n2) SC = O(1)
        # max_area = 0
        # current_area = 0
        # for i in range(n):
        #     for j in range(i+1, n):
        #         current_height = min(height[i], height[j])
        #         current_width = j - i
        #         current_area = current_height * current_width
        #         max_area = max(max_area, current_area)
        # return max_area

        ### Optimal
        ### TC = O(n) SC = O(1)
        max_area = 0
        current_area = 0
        left = 0
        right = n-1

        while left < right:
            current_width = right - left
            current_height = min(height[left], height[right])
            current_area = current_width * current_height
            max_area = max(current_area, max_area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return max_area

