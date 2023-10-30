'''
Program to count number of operations to empty an array.
'''

def countOperationsToEmptyArray(nums):
    arr=[*nums] 
    nums.sort()
    cnt=0
    while(len(arr)>0):
        cnt+=1
        if arr[0]==nums[0]:
            nums.remove(nums[0])
            arr.remove(arr[0])
            print(len(arr))  
            
        else:
            t=arr[0]
            arr.remove(arr[0])
            arr.append(t)
            print(len(arr))
        
    return cnt
            
print(countOperationsToEmptyArray([3,4,-1]))

