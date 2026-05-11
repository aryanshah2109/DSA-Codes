class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)

        ## Brute
        ## TC = O(n3 * log(unique elements)) SC = O(n)
        # answer = []
        # for i in range(n): 
        #     for j in range(n):
        #         for k in range(n):
        #             if (
        #                 i != j and
        #                 j != k and
        #                 i != k and
        #                 nums[i] + nums[j] + nums[k] == 0
        #             ):

        #                 temp = sorted([nums[i], nums[j], nums[k]])

        #                 if temp not in answer:
        #                     answer.append(temp)
        # return list(answer)


        ## Better
        ## TC = O(n2) SC = O(n)        
        # answer = set()

        # for i in range(n):
        #     hashset = set()
        #     for j in range(i+1, n):
        #         search = -1 * (nums[i] + nums[j])

        #         if search in hashset:
        #             candidate = tuple(sorted([nums[i], nums[j], search]))

        #             answer.add(candidate)
                
        #         else:
        #             hashset.add(nums[j])
        # return [list(x) for x in answer]

        ## Optimal
        ## TC = O(nlogn) + O(n2)
        ## SC = O(n)

        # Sort array
        nums.sort()

        answer = set()
        for i in range(n):

            if i > 0 and nums[i] == nums[i-1]:
                continue

            j = i + 1
            k = n - 1
            while j < k:
                candidate_sum = nums[i] + nums[j] + nums[k]

                if candidate_sum < 0:
                    j += 1
                elif candidate_sum > 0:
                    k -= 1
                else:
                    answer.add((nums[i], nums[j], nums[k]))
                    j += 1
                    k -= 1

                    while j < k and nums[j] == nums[j-1]:
                        j += 1
                    while j < k and nums[k] == nums[k+1]:
                        k -= 1
        
        return [list(x) for x in answer]