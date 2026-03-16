
def nextGreaterElement(self, nums1):
    """
    :type nums1: List[int]
    :rtype: List[int]
    """
    
    ## Brute: TC = O(n2) SC = O(n)
    ## Create 2 loops, for each element, scan from i+1 to end for first maximum and then break

    ## Optimal: TC = O(N) SC = O(2N)

    nge = [-1] * len(nums1)
    stack = []

    for i in range(len(nums1) - 1, -1, -1):
        
        while len(stack) != 0 and stack[-1] <= nums1[i]:
            stack.pop(-1)

        if len(stack) != 0:                   
            nge[i] = stack[-1]

        stack.append(nums1[i])

    return nge