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

####### WHILE LOOP ##########
n=10
i=1
while(i<n):
    print(i)
    i=i+1

####### ANOTHER TASK USING EWHILE LOOP ################
joining_age=25
retirement_age=60
while(joining_age<retirement_age):
    print(joining_age)
    joining_age=joining_age+1
else:
    print("Now, It's Time to retire...")

######## ATM MACHINE ############
total_amount=int(input("Enter the Total Amount: "))
while(total_amount!=0):
    print(total_amount)
    total_amount=total_amount-100
else:
    print("Please put more Money in the ATM machine.")


######### FOR LOOP #############
list=["shally","Mummy","ujjwal","maheshwari","Harpreet",2,3.5,4+9j]
for i in list:
    print(i)

###### TASK ############
l=["Mango","Cherry","Banana","Papaya"]
for i in l:
    print(i)
    if l=="Cherry":
        print("The above fruit is Cherry.")
l[0]="Strawberry"
print(l)

#####################################
a="Shally Nagfase"
for i in a:
    print(i)
print(a[2])


####### RANGE ########
for i in range(0,12,2): # START, END, DIFFERENCE
    print(i)

######### Patterns using Nested Loops ##########
n=7
for i in range(0,n):
    for j in range(0,i+1):
        print("* ",end="")
        print("\r")

n=7
for i in range(0,n):
    for j in range(0,i+1):
        print(" * ",end="")
    print("\r")

# BREAK
list=[1,2,3,4,5,"Shally","Harpreet"]    # The loop breaks after shally is printed
for i in list:                          # In break it will skip the entire Loop
  print(i)
  if i=="Shally":
    break

# CONTINUE
list=[1,2,3,4,5,"Shally","Harpreet"]     # Shally is not getting printed in the output
for i in list:                           # In continue it will skip one step which ever step is running based on condition
  if i=="Shally":
    print("The name is Shally")
    continue
  print(i)

# PASS
list=[1,2,3,4,5,"Shally","Harpreet"]         # Shally is getting printed in the output
for i in list:
  if i=="Shally":
    print("The name is Shally")
    pass
  print(i)

######### Patterns using Nested Loops(EUQILATERAL TRIANGLE) ##########
size = int(input("Enter the size of the equilateral triangle: "))
for i in range(size):
    for j in range(size-i):
        print("",end=" ")
    for k in range(i+1):
        print("*",end="")
    for m in range(k-1):
        print("*",end="")
    print()

# Method 2
n = 20
for i in range(n):
    print(" "*(n-i),end="")
    for j in range(i*2+1):
            print("*",end="")

    print()

