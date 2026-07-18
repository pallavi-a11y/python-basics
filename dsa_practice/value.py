#Count how many numbers are **greater than a given value** 
arr=[5,6,9,10,17,18,20]
value=7
count=0
for i in range(len(arr)):
    if arr[i]>value:
        count=count+1

print(f"the count of numbers gteater than given value : {count}")
