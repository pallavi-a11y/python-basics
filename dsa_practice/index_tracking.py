#**Index-tracking pattern (useful for later LeetCode problems):**
# Find the **index** of the largest number (not the value — the position)
# Check if a specific number **exists** in the array (return True/False)
# Find the **first** number in the array that is greater than 10
arr=[3, 5, 11, 56, 76, 98, 34]
largest=arr[0]
largest_index=0
exist=76
found=False
for i in range(len(arr)):
    if arr[i]>largest:
        largest=arr[i]
        largest_index=i
print(largest)
print(f"the largest elements index : {largest_index}")
for j in range(len(arr)):
    if exist==arr[j]:
        found=True
print(found)

first=arr[0]
for k in range(len(arr)):
    if arr[k]>10:
        first= arr[k]
        break
print(first)



