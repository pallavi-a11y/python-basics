""" {n= int(input("enter n"))
i=1
while i<=n:
    if(1<=n<=100):
        print("*" *n)
    i=i+1
exit()}
"""
#correted way
n= int(input("enter n :"))
if 1<=n<=100:
    i=0
    while i<n:
        print("*" *n)
        i=i+1
    

    