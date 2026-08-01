#23. Rotate an array by 1 position to the right (e.g. [1,2,3,4,5] → [5,1,2,3,4])
a=[1,2,3,4,5]
for i in range(len(a)):
    for j in range(len(a),0 ,-1):
        a[j] = a[i]
print(a)