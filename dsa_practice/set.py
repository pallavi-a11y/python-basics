# goal: print {1, 2, 3, 4, 5}
'''a = [1, 2, 2, 3, 4, 4, 5]
My_set= set()
dup=False
for i in range (len(a)):
    if a[i] in My_set:
        dup=True
    else:
        My_set.add(a[i])
print(My_set)'''
a = [1, 2, 2, 3, 4, 4, 5]
My_set = set()
for i in range(len(a)):
    My_set.add(a[i])
print(My_set)