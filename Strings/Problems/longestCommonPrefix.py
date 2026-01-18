def longestCommonPrefix(strs: list):
    """
    :type strs: List[str]
    :rtype: str
    """
    ## Brute Force:
    ## take each string of the array and manually compare all characters and append in the
    ## result string if the common prefix exists in all. 

    ## Optimal: TC = O(nlogn) SC = O(1)
    ## Sort the array. Compare only first and last string of sorted array.
    ## Any common prefix bw first and last will also be common in the 
    ## middle strings. So now only compare first and last strings for
    ## common prefixes

    lcp = ""

    strs.sort()

    a = strs[0]
    b = strs[-1]

    for i in range(min(len(a), len(b))):
        if a[i] == b[i]:
            lcp += a[i]
        else:
            break        
    return lcp
        
print(longestCommonPrefix(["flower","flow","flight"]))