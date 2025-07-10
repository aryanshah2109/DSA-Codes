def maxConsecutiveOnes(nums):
    count = 0
    maxCount = 0
    
    for i in range(len(nums)):
        if(nums[i] == 1):
            count+=1
        else:
            count = 0
        if(maxCount < count):
            maxCount = count
    
    return maxCount

print(maxConsecutiveOnes([1,1,0,1,1,1,0,1,1,1,1]))