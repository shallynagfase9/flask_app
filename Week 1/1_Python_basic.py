a=10
print(a)
print(type(a))

b=12.3
print(b)
print(type(b))

c="shally"
print(c)
print(type(c))

d=True
print(d)
print(type(d))

c1=True-False     #Value of True is considered as 1 and value of False as 0
print(c1)         #1-0=1
c2=True*False
print(c2)

e=4+9j
print(type(e))
print(e.real)  #It will print the real number from my complex number
print(e.imag)  #It will extract the imaginary part of my complex number

a=10
b="shally"
print(str(a) +b)  #For performing concatenation or any other operation
#both the values should be of the same data type

a=int(input("Enter the value of a: "))
b=int((input("Enter the value of b: ")))
c=a+b
print(c)
