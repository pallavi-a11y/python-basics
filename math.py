# here is some inbulit function that we use from the math class for that we import that class
import math 
a= math.pi
print(a)
print(math.e)
print(math.ceil(a))
print(math.floor(a))
# application of the math class 
#calculating the circumference and area of the circle
r= float(input("enter the value of radius :"))
result= 2*math.pi*r
result=round(result,2)
print(f"the circumference of the circle is :{result} cm")
area= pow(r,2)* math.pi
area=round(area,2)
print(f"the area of the circle is :{area} cm**2")

# we can also calculate the hypotaneous of the right angle triangle
p= float(input("enter the prependicular:"))
b=float(input("enter the base:"))
h=math.sqrt(pow(p,2)+pow(b,2))
print(f"the hypotaneous of the triangle is :{h}cm ")
#these are some use case of that