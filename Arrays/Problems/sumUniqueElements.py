# You are given an integer array nums. The unique elements of an array are the elements that appear 
# exactly once in the array. Return the sum of all the unique elements of nums. 


def sumOfUnique( nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    n = len(nums)

    ## Approach 1: TC = O(n2) SC = O(1)
    # sum = 0
    # for i in range(n):
    #     isUnique = True
    #     for j in range(n):
    #         if nums[i] == nums[j] and i != j:
    #             isUnique = False
    #     if isUnique:
    #         sum += nums[i]

    # return sum

    # Approach 2: TC = O(n), SC = O(n)
    hashmap = {}
    for i in range(n):
        if nums[i] in hashmap:
            hashmap[nums[i]] += 1
        else:
            hashmap[nums[i]] = 1

    unique = []
    for key, value in hashmap.items():
        if value == 1:
            unique.append(key)
    
    sum = 0
    for i in range(len(unique)):
        sum += unique[i]

    return sum


print(sumOfUnique([1,2,3,2]))