## Longest substring with k unique elements
## Eg: 
## s = "aabacbebebe"
## k = 3 
## O/P -> 7. substr = cbebebe


def brute(s: str, k: int):
    ## TC = O(n2) SC = O(n)
    
    n = len(s)
    max_len = 0
    current_len = 0
    for i in range(n):
        substr_set = set()
        substr = ""
        for j in range(i,n):
            substr += s[j]
            substr_set.add(s[j])
            if len(substr_set) == k:
                current_len = len(substr)
                max_len = max(current_len, max_len)
    return max_len

def optimal(s: str, k:int):
    ## TC = O(n) SC = O(n)
    
    n = len(s)
    
    i = 0
    j = 0
    max_len = 0
    current_len = 0
    substr_unique = {}

    while j < n:
        
        if s[j] not in substr_unique:
            substr_unique[s[j]] = 1
        else:
            substr_unique[s[j]] += 1
        
        while len(substr_unique) > k:
            substr_unique[s[i]] -= 1
            if substr_unique[s[i]] <= 0:
                del substr_unique[s[i]]
                
            i += 1
        
        if len(substr_unique) == k:
            current_len = j - i + 1
            max_len = max(max_len, current_len)
        
        j += 1
    
    return max_len
        


s = "aabacbebebe"
k = 3
print(brute(s,k))
print(optimal(s,k))

