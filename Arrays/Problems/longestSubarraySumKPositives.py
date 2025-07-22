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

arr = [1,2,3,1,1,1,1,4,2,3]
k = int(input("Enter k: "))

maxLen = longestSubarrayBrute(arr,k)
print(maxLen)

maxLen = longestSubarrayBetter(arr,k)
print(maxLen)