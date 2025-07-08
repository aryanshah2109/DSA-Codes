arr = [1,2,2,3]

n = len(arr)

# Brute Force
# temp = []
# for i in range(n):
#     if(nums[i]!=0):
#         temp.append(nums[i])
        
# for i in range(n):
#     if(i<len(temp)):
#         nums[i] = temp[i]
#     else:
#         nums[i] = 0
# print(nums)

j = -1

for i in range(n):
    if(arr[i] == 0):
        j = i
        break
 
if j == -1: # no zeroes found
    print(arr)
    raise SystemExit(1)
    
for i in range(j+1,n):
    if(arr[i] != 0):
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp
        j+=1
print(arr)


            
            
            
            
            
            
            
            