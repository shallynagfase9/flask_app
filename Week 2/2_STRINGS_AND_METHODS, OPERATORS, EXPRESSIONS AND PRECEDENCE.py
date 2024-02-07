#################### STRINGS AND METHODS, OPERATORS, EXPRESSIONS AND PRECEDENCE ##########################

c = True and True
print(c)

d = True or False
print(d)

a = False or False
print(a)

b = not True
print(b)

## LET'S DEFINE TWO VARIABLES HAVING BOOLEAN VALUES ##
Start=True 
Stop=False
print(f"Defined value of Start is {Start}")
print(f"Defined value of Stop is {Stop} \n")

print(f"Defined value of Start is {Start}")
print(f"Defined value of Stop by negating Start is { not Start} \n")

print(f"Defined value of Start by negating Stop is {not Stop}")
print(f"Defined value of Stop is {int (not Stop)} \n")

k = not 0
print(k)

m = not 1
print(m)

n = not(int("123"))
print(n)

l = not int(bool (1))
print(l)

k = bool(-5)  # Boolean value of any number will be True except 0
print(k)

t = bool(5)
print(t)


###################################
zero = 0
one = 1
print(f"Boolean value of no. {zero} is {bool (zero)}")
print(f"Boolean value of no. {one} is {bool (one)}")
print(f"Negation of {zero} is {not zero} and Negation of {one} is {not one} ")

####################################
vegetables = True
salt = False 
dish = vegetables and salt
print(f"Dish contains vegetables: {vegetables}")
print(f"Dish contains salt: {salt}")
print(f"Hence Dish prepared was good: {vegetables and salt}")

####################################
list_a = [1,2,3,4]      # We can find the memeory address of the object by using function (id).
list_b = [1,2,3,4]        # List is a collection of elements of different types and is mutable
print(id(list_a))
print(id(list_b))
print(list_a is list_b)
list_b = list_a   # Address becomes same after both the object becomes equal
print(id(list_a))
print(id(list_b))


########################################
str1="shally"
str2="nagfase"
print(id(str1))
print(id(str2))

###### Operators ######
max_speed_of_car = 200
max_speed_of_bike = 100
print(f"Bike is faster than Car: {max_speed_of_car < max_speed_of_bike}")

########################
list_a = [1,2,3,4,5,"shally"]
list_b = [1,2,3,4,5,"shally"]
print(list_a is not list_b)
print(list_a == list_b)
print(id(list_a))   # id() built-in function will display the id(Memory address) at which the list is stored
print(id(list_b))