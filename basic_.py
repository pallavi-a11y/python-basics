#this is the basic program that include  comments,variables,type casting and,input programs .....
# comments: we use "#" to write a comment 
# variables = they contain a valuse and act as their type integer float sttring and boolean 
#f-string = it is used form formatting we use {} and write the variable we want to add or display
first_name="pops"
print(f"hello {first_name}!")
print("so greate to see u here")

food= "allo tikki"
print(f"{first_name} likes {food}")

# string is a sequence of same type char or values
#int is the integer value or whole value while  float is a decimal point value
#boolean have only two values True and False

price= 25
print(f"the price of {food} is {price}")

is_tasty= True
if is_tasty:
    print(f"{food} is worth eating")
else:
    print(" dont waste ur money bruhhhh")

#types and type casting  int(),float(),str(),bool()
name= "pops"
age ="23"
username= name + age
print(f" {name} and {age} can make the usre name {username}")

# here the thing is both name and age are string if 
student= "pops"
gpa= 8.5
print(f"the student {student} has gpa {gpa}")
sum = int(age) + int(gpa) # got an error as the type of them are differnt using int() will remove type error
print("sum is", sum+ int(age))
print("sum is", sum,age)
print("sum is", sum,"and age is",age)

# bool() type cast is mostly used for the checking if the person has input the value wher vale is mandatory to enter as in name if value is null it will print  false else its true


# input : a function that prompts user input data 

# default return is string 
name = input("enter the name")
age=input(" enter age")
age=int(age)
print(type(age))# it will return the string using int() typecasting we make datatype right 
# we will use this basics in further exercises ...........