# find unique element in constant space and linear time complexity
def unique(nums):
    answer = 0
    for i in nums:
        answer = answer ^ i
    return answer
print(unique([1,5,1,3,5]))