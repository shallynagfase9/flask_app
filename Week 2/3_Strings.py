c=int("123")   #It will convert the string into integer
print(c)   

d=float("123")   #It will convert the string into float
print(d)  

e=bool(1)  #It will covert integer into bool
print(e)

age=20
print(f"My age is {age}")  # f is used for formatting

name="shally"
city="Nagpur"
print("my name is {} and I live in {}".format(name,city))  # Another way of formatting

name="Sunita"
age=42
Degree="Btech"
print("My age is {} and I have completed: the degree of {} with name {} ".format(age,Degree,name))

name="Ujjwal"
age=22
Degree="Btech"
print(f"My age is {age} and I have completed: the degree of {Degree} with name {name} ")

########## Control Flow #############
age=int(input("Enter the age of a person: "))
if age>=18 and age<=45:
    print("You're are a young blood.")
else:
    print("Thank you we'll let you know.")

################## ASSIGNMENT #####################
product_price=int(input("Enter the product price: "))
if product_price>1000:
    print(f"The price of the product is {product_price-(product_price*0.2)} Rs.") # 20% off on product price if price is greater than 1000 
else:
    print(f"The product price is {product_price-(product_price*0.3)} Rs.")  # 30% off on product price if price is less than 1000 

########## ANOTHER WAY OF FORMATTING ##############
product_price=int(input("Enter the product price: "))
if product_price>3000 and product_price<10000:
    print("The price of the product is {} Rs.".format(product_price-(product_price*0.2))) # 20% off on product price if price is greater than 1000 
elif product_price>2000 and product_price<=3000:
    print("The product price is {} Rs.".format(product_price-(product_price*0.3)))  # 30% off on product price if price is less than 1000 
elif product_price>=100000:
    print("Congratulations!! You won additional gift with Discount.")
else:
    print("Let's drink Green tea.")


########### SINGLE STATEMENT #############
value=int(input("Enter a number: "))
if(value<=1000): print("The value is less than or equal to 1000.")
else:
    print("It's Greater than 1000")

