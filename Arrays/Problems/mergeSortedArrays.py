class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        ## Brute
        ## TC = O(m + n) SC = O(m)

        # nums3 = []
        # i = 0
        # j = 0
        # while i<m and j < n:
        #     if nums1[i] <= nums2[j]:
        #         nums3.append(nums1[i])
        #         i += 1
        #     else:
        #         nums3.append(nums2[j])
        #         j += 1
        
        # while i<m:
        #     nums3.append(nums1[i])
        #     i+=1
        # while j<n:
        #     nums3.append(nums2[j])
        #     j+=1
        
        # for k in range(len(nums3)):
        #     nums1[k] = nums3[k]
        
        # return 


        ## Optimal
        ## TC = O(m + n) SC = O(1)

        # Start from end
        i = m - 1
        j = n - 1
        k = m + n - 1

        while i >= 0 and j >= 0:
            if nums1[i] >= nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1
        
        # remaning nums2 elements
        while j>=0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1
        
        return 