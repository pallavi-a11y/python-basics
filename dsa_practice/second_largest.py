#to find the secound largest no in the array
arr=[3,5,7,9,8,3]
largest=arr[0]
second=arr[0]
for i in range(len(arr)):
    if arr[i]>largest:
        second= largest
        largest= arr[i]
    elif arr[i]>second and arr[i]< largest:
        secound=arr[i]
print(f"the largest no :{largest},\n the second largest no :{second}")