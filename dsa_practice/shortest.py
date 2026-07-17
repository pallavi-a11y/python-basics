#Find the smallest number in an array
arr=[3,6,1,8,9,0]
smallest=arr[0]
for i in range(len(arr)):
    if arr[i]<smallest:
        smallest= arr[i]
print(f"the smallest value is {smallest}")