def MyFunction():
    return("catch me if u can ")
Done=MyFunction()
print(f"{Done}")

#python compound interset calculator 
principal= float(input("enter the principal balance" ))
r=float(input("enter the rate" ))
t=float(input("enter the time period " ))
while principal <0:
    if principal<0:
        print("principal cant be less0")
while r<0:
    if r<0:
        print("rate cant be less than")
while t <0:
    if t<0:
        print("time cant be less than ")

total=principal*pow((1+(r/100)),t)
print(f"balance after {t} year/s :${total:.2f}")

    