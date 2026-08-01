#22. Find the number that appears only once in an array where every other number appears twice (try without extra data structures first, then look up XOR trick after)
a=[1,2,3,4,4,3,2,1,9]
count={}
for i in range(len(a)):
    if a[i] in count:
        count[a[i]]=count[a[i]]+1
    else:
        count[a[i]]=1
for key in count:
    if count[key]==1: 
        print(key)