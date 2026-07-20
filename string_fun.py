#string functions
name= input("enter the name")
result=len(name) # to find the length oof string
print(result)
result=name.find("a") # find the first index of the elemnt 
print(result)
result=name.rfind("a")#find the last index oof the element works as for the reserve
print(result)
#print(help(str)) #prints all the string fun
result=name.capitalize( )
print(result)
result=name.upper()
print(result)
result=name.lower()
print(result)
name= input("enter the name")
result=name.isdigit()
print(result)
result=name.isalpha()
print(result)
phone_no=input("enter the phone no")
c= phone_no.count("-")
print(c)
result=phone_no.replace("-","")
print(result)