#Find the **sum** of all elements in an array
#Find the **average** of all elements in an array
arr=[2,4,5,6,7,9]
sum=0
for i in range(len(arr)):
    sum= sum +arr[i]
print(f"the sum of the elements of array is: {sum}")
avg = sum/ len(arr)
print(f"the avg of the elements is :{avg}")