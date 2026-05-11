class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)

        ## Brute
        ## TC = O(n + nlogn) SC = O(n)
        # answer = []
        # for i in range(n):
        #     answer.append(nums[i] ** 2)
        # answer.sort()
        # return answer

        ## Optimal

        left = 0
        right = n-1
        answer = [0] * n
        index = n-1

        while left <= right:
            leftSq = nums[left] ** 2
            rightSq = nums[right] ** 2

            if leftSq < rightSq:
                answer[index] = rightSq
                right -= 1
            else:
                answer[index] = leftSq
                left += 1

            index -= 1

        return answer