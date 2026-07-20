#19. Given a sorted array and a target sum, find two numbers that add up to the 
#target (two-pointer approach, not brute force nested loop)
arr=[1,2,3,4,6,8,9]
target=12
n=len(arr)
i=0
j=n-1
find_sum=False
while i < j :
    sum=arr[i]+arr[j]
    if sum==target:
       find_sum=True
       break
    elif sum< target:
        i=i-1
    else:
        j=j-1
if find_sum:
    print("the target is found")
else:
    print("the target is  not found")