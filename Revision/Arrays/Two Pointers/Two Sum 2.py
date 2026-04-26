class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        ## Brute:
        ## TC = O(n2) SC = O(1)
        # for i in range(len(numbers)):
        #     hasTarget = False
        #     for j in range(i+1, len(numbers)):
        #         if numbers[i] + numbers[j] == target:
        #             hasTarget = True
        #             return [i+1, j+1]
            
        # return []

        ## Better
        ## TC = O(n) SC = O(n)

        # hashmap = {}
        # for i in range(len(numbers)):
        #     if target - numbers[i] in hashmap:
        #         return sorted([i+ 1, hashmap[target - numbers[i]] + 1])
        #     else:
        #         hashmap.update({
        #             numbers[i] : i
        #         })
        # return []

        ## Optimal: As sorted array always
        ## TC = O(n) SC = O(1)

        left = 0
        right = len(numbers) - 1

        while left < right:
            if numbers[left] + numbers[right] == target:
                return [left + 1, right + 1]
            elif numbers[left] + numbers[right] < target:
                left += 1
            else:
                right -= 1
        return []
