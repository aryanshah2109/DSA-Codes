def unique(nums):
    temp = {}
    for i in range(len(nums)):
        count = 0

        if nums[i] in temp.keys():
            temp[nums[i]] += 1
        else:
            temp.update({nums[i]:1})


    for key,value in temp.items():
        if value == 1:
            return key

print(unique([1,1,2,2,3,4,4]))

def uniqueBrute(nums):
    n = len(nums)

    for i in range(n):
        isUnique = True

        for j in range(n):
            if i != j and nums[i] == nums[j]:
                isUnique = False
        
        if isUnique:
            return nums[i]
        
print(uniqueBrute([1,1,2,2,3,4,4]))