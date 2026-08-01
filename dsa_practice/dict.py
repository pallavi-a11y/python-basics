a=[3,5,6,2,7,9]
target=8
m={}
for i in range(len(a)):
    need= target-a[i]
    if need in  m:
        print("found pair", need ,a[i])
    else:
        m[a[i]]=i