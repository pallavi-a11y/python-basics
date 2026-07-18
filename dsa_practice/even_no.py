#Count how many **even** numbers are in an array 
arr=[6,3,7,8,2,4]
count=0
for i in range(len(arr)):
    if arr[i]%2==0:
        count= count+1
    
print(f"the count of even no are {count}")
