#next topic is logical operator  : 3 type of operator : and ,or ,not
#lets check with example
temp=float(input("enter the temprature"))
is_raning=False
if temp>30 or is_raning:
    print("the event is cancel")
elif 30>temp>20 and not is_raning:
    print("event will be continuing")

#conditional expression 
# one line shortcut for the if _else statement 
# we use the one line shortcut writing
#X if conditon else Y
num=int(input("enter the number"))
result= "positive"if num>0 else "negative"
print(result)
num =int(input("enter the number"))
result= "positive"if num>0 else "negative"
print(result)
temp= float(input("enter the temprature"))
result="hot"if temp>25 else"cold"
print(result)
a=int(input("enter the no1"))
b=int(input("enter the no2"))
max_no=a if a>b else b
print(max_no)
min_no=a if a>b else b
print(min_no)
