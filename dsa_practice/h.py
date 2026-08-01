a = [1,2,3,3,4]
my_set= set()
dup=False
for  i in range(len(a)):
    if a[i] in my_set:
        dup=True
    else:
        my_set.add(a[i])
print(dup)


