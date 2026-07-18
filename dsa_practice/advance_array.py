#**Slightly harder — combine two conditions:**
#13. Count how many numbers are **both even AND greater than 5**
#14. Find the largest **even** number in the array (skip odd numbers while comparing)
#**Two-array comparison:**
#15. Given two arrays of the same length, find how many positions have the **same value** at the same index
arr=[2,5,4,1,7,8,9,10,6]
count=0
largest=arr[0]
for i in range(len(arr)):
    if arr[i]%2==0 and arr[i]>5:
        count=count+1
print(f"the count of the numbers that are even and greter than 5 :{count}")
for j in range(len(arr)):
    if arr[j]%2==0 and arr[j]>largest:
        largest = arr[j]
print(f"the largest even no is {largest}")

a1=[4,6,7,8,2,5]
a2=[7,6,4,8,5,2]
index =0
count=0
for i in range(len(a1)):
        if a1[i]== a2[i]:
            index=i
            coun=count+1
            print(f"the position tha have the same index {index}")
print(f"no of same elements at same index {count}")