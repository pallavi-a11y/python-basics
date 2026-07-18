#Reverse an array in place (without using arr[::-1] or .reverse() — 
#swap elements manually using two pointers, one from start, one from end)
import math
arr=[1,2,3,4,5,6,7,8,9,10]
i=0
j= len(arr)-1
while i<j:
    temp=arr[i]
    arr[i]=arr[j]
    arr[j]=temp
    i=i+1
    j=j-1
print(arr)

# using for loop
n=len(arr)
j=n-1
for i in range(math.floor(n/2)): #or i can use (n//2) returns int value
    temp=arr[i]
    arr[i]=arr[j]
    arr[j]=temp
    j=j-1
print(arr)     