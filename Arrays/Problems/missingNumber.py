def missingNo(nums, n):
    sumReal = (n*(n+1))//2
    sumActual = 0
    for i in nums:
        sumActual += i
    return sumReal - sumActual

nums = [1,3,4,5]
print(missingNo(nums,5))