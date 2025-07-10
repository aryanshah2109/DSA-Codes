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


def unionOptimal(nums1,nums2):
    nums3 = []
    i = 0
    j = 0
    k = 0
    n = len(nums1)
    m = len(nums2)

    while(i<n and j<m):
        if(nums1[i] <= nums2[j]):
            if(k==0 or nums3[k-1] != nums1[i]):
                nums3.append(nums1[i])
                k+=1
            i+=1
        else:
            if(k==0 or nums3[k-1]!=nums2[j]):
                nums3.append(nums2[j])
                k+=1
            j+=1

    if i>=n:
        while(j<m):
            if(k==0 or nums3[k-1]!=nums2[j]):
                nums3.append(nums2[j])
                k+=1
            j+=1
    if j>=m:
        while(i<n):
            if(k==0 or nums3[k-1] != nums1[i]):
                nums3.append(nums1[i])
                k+=1
            i+=1
    
    return nums3

nums1 = [1, 2, 3, 4, 5, 9]
nums2 = [1, 2, 6, 7]

nums3 = union(nums1,nums2)
print(nums3)
nums3 = unionOptimal(nums1,nums2)
print(nums3)
