# to find the largest no in the array
arr=[3,7,8,9,2,4]
largest=arr[0]
for i in range(len(arr)):
    if arr[i]>largest:
        largest= arr[i]
print(f"the largest no in the array is : {largest}")

