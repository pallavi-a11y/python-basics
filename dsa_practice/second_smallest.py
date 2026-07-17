#Find the **second smallest** number in an array
arr=[10,9,1,4,6,8]
smallest=arr[0]
second=arr[0]
for i in range(len(arr)):
    if arr[i]<smallest:
        secound=smallest
        smallest=arr[i]
    elif arr[i]<second and arr[i]>smallest:
        second=arr[i]
print(f"the smallest no is {smallest},\n the second smallest no is {second}")