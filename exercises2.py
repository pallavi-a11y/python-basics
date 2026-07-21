#python weight convertor program
weight=float(input("enter the weight: "))
unit=input("enter the unit kg/lbs: ")
if unit=="kg":
    weight=weight*2.205
    unit="lbs"
elif unit=="lbs":
    weight=round(weight/2.205,2)
    unit="kg"
print(f"the weight is {weight}{unit}")

#temprature conversion program
temp=float(input("enter the temprature : "))
unit=input("enter the unit C/F: ")
if unit=="C":
    temp=round((temp*9/5)+32,2)
    unit="F"
elif unit=="F":
    temp=round((temp-32)*5/9,2)
    unit="C"
print(f"the temprature is {temp}{unit}")