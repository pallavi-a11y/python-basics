#Given an array, move all zeros to the end while keeping the order 
#of other elements (e.g. [0,1,0,3,12] → [1,3,12,0,0])
arr=[0,1,0,3,12]
result=[]
count=0
for i in range(len(arr)):
    if arr[i]==0:
        count=count+1
    elif arr[i]!=0:
        result.append(arr[i])
for i in range(count):
    result.append(0)
print(result)