def intersection(nums1,nums2):
    n = len(nums1)
    m = len(nums2)

    i = 0
    j = 0

    # Brute force
    s = set()
    for i in range(len(nums1)):
        if nums1[i] in nums2:
            s.add(nums1[i])
    return list(s)




nums1 = [1,1,3,4,4,5,6,9]
nums2 = [1,2,2,3,6,7,8]
nums3 = intersection(nums1,nums2)
print(nums3)
