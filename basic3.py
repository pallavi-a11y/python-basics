#we use control staements like if elif and else 
age =int(input("enter the age "))
if age>100:
    print("just die for god sake")
elif age >= 18:
    print("u are qualified to subscribe")
elif age< 18:
    print("still a child hah!")
else:
    print("did u van born yet")

#the other is we can use the boolean value 
is_sale= True
if is_sale:
    print("the item is avilable")
else:
    print("the item is not avilable yet ")

#next is check for the null name entry
name= input("enter ur name")
if name== "":
    print("enter ur funking name bitch")
else:
    print(f"hello {name} ..how are u doing")


#lets make a calculator using control statement and arithematic operations 
opn=input("select the operation +,-,*,/,**,%")
a= float(input("enter the number :"))
b= float(input("enter the number :"))
if opn== "+":
    result=a+b
    print(f"the addition is {result}")
elif opn== "-":
    result=a-b
    print(f"the substraction is {result}")
elif opn== "*":
    result=a*b
    print(f"the multipliction is {result}")
elif opn== "/":
    result=a/b
    print(f"the division is {result}")
elif opn== "%":
    result=a%b
    print(f"the remainder is {result}")
else :
    result=a**2
    print(f"the square is {result}")
