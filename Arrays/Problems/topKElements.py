class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        ## 
        ##
        hashmap = {}
        for i in range(n):
            if nums[i] in hashmap:
                hashmap[nums[i]] += 1
            else:
                hashmap[nums[i]] = 1
        sorted_hashmap_list = sorted(hashmap.items(), key=lambda item: item[1], reverse=True)
        sorted_hashmap = dict(sorted_hashmap_list)
        ans = []
        for key in sorted_hashmap.keys():
            if len(ans) < k:
                ans.append(key)

        return ans


