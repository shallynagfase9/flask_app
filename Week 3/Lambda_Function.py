n = 2
p = 4
def test(n,p):
    return n**p
print(test(2,4))

# Lambda function 
a = lambda n,p: n**p # this kind of function is called lambda function
print(a(2,3))

# Addition using lambda function
b = lambda a,b: a+b
print(b(243,13))

# converting celsius to farheneit using lambda function
c_to_f = lambda c: (9/5)*c + 32
print(c_to_f(34)) 

# Finding maximum numeric value between two numbers
d = lambda x,y: x if x>y else y
print(d(34,56))

# Finding length of string using Lambda function
s = 'Shally Nagfase'
l = lambda s: len(s)
print(l(s))