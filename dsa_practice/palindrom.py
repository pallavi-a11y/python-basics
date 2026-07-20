#18. Check if an array is a palindrome (reads the same forwards and backwards) — use two pointers moving toward each other
arr=[9,8,7,6,5,6,7,8,9]
n=len(arr)
i=0
j=n-1
element_found= True 
while i<j :
    if arr[i]==arr[j]:
        i=i+1
        j=j-1
    else:
        i=i+1
        j=j-1
        element_found=False
                
if element_found:
    print("the arry is  a palindrom")
else:
    print("the arry is not a palindrom")
        
