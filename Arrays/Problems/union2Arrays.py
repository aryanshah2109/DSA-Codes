# Brute Force
def union(nums1,nums2):
    nums3 = set()
    i=0
    j=0
    n=len(nums1)
    m=len(nums2)
    while i<n:
        nums3.add(nums1[i])
        i+=1
    while j<m:
        nums3.add(nums2[j])
        j+=1
    return list(nums3)
    

nums1 = [1, 2, 3, 4, 5]
nums2 = [1, 2, 7]

nums3 = union(nums1,nums2)
print(nums3)