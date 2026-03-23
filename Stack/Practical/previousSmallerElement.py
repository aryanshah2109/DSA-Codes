def previous_smaller_element(nums):
    n = len(nums)
    
    ## Brute
    ## TC = O(n2) SC = O(n)
    # nge = []
    # for i in range(n):
    #     found = False
    #     for j in range(i-1, -1, -1):
    #         if nums[i] > nums[j]:
    #             nge.append(nums[j])
    #             found = True
    #             break
    #     if not found:
    #         nge.append(-1)
    # return nge
    
    ## Optimal
    ## TC = O(n) SC = O(2n)
    nge = []
    stack = []
    
    for i in range(n):
        while len(stack) != 0 and stack[-1] >= nums[i]:
            stack.pop(-1)
        if len(stack) == 0:
            nge.append(-1)
        else:
            nge.append(stack[-1])
        stack.append(nums[i])
    return nge
    
    
print(previous_smaller_element([4,5,2,10,8]))
                
# [-1, 4, -1, 2, 2]