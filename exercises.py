# exercis to cover the input part
#area of a rectangle

length= int(input("enter the length"))
bredth= int(input("enter the bredth"))
area = length * bredth 
#now the thing is that we use int() cause there in no muliplication btw string and string sequence 
print(area)

#shopping cart program
item = input("enter the item name ")
price = int (input("enter the price"))
quantity= int(input ("enter the quantity"))
total= price* quantity
print(f"you have bought {quantity} of the {item}")
print(f"total amount t be paid: {total}")



