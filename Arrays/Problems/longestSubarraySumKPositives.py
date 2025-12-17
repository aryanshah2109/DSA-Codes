# Only positives in array

def longestSubarrayBrute(arr,k):
    # O(n3) TC 
    # O(1) SC
    n = len(arr)
    maxLen = 0
    givenLen = 0
    for i in range(n):
        for j in range(i,n):   
            subarray = [arr[k] for k in range(i,j+1)]
            givenLen = len(subarray)
            if sum(subarray)==k and givenLen>maxLen:
                maxLen = givenLen
                
    return maxLen

def longestSubarrayBetter(arr,k):
    # O(n2) TC 
    # O(1) SC
    n = len(arr)
    maxLen = 0
    givenLen = 0    
    for i in range(n):
        sum = 0
        for j in range(i,n):   
            sum += arr[j]
            givenLen = j-i+1
            if sum==k and givenLen>maxLen:
                maxLen = givenLen
                
    return maxLen


def longestSubarrayOptimal(arr,k):
    # TC = O(2n) :
    # 2n even though 2 loops as i and j are moving independant of each other and i doesnt reset for any j
    
    # SC = O(1)
    n = len(arr)

    i = 0
    j = 0
    local_sum = 0
    max_window_size = 0

    while j < n:
        local_sum += arr[j]

        if local_sum > k:

            while local_sum > k:
                
                local_sum -= arr[i]
                i += 1

        if local_sum == k:
            max_window_size = max(j-i+1, max_window_size)
        
        j += 1

    return max_window_size

arr = [1,2,3,1,1,1,1,4,2,3]
k = int(input("Enter k: "))

maxLen = longestSubarrayBrute(arr,k)
print(maxLen)

maxLen = longestSubarrayBetter(arr,k)
print(maxLen)

maxLen = longestSubarrayOptimal(arr,k)
print(maxLen)
