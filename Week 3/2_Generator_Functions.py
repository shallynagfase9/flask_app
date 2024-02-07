# range will give you one by one generating data by iteration
for i in range(0,11):
    print(i)

list = [1,2,3,4,5,6,[3,45,6,53,434]]
def test(list):
    n = []
    for i in list:
        if type(i)==int:
            n.append(i)
    return(n)
print(test(list))


## Example of generator functions
## fibonacci series Example. (Fibonacci series is the addition of previous two numbers.)
def test1(n):
    a,b=0,1
    for i in range(n):
        yield a       # yield is used to create a generator function
        a,b=b,a+b
print(test1(12))
for i in test1(12):
    print(i)

# fabonacci series formula explanation:
# formula : a,b = b, a+b
"""
Suppose a = 0, b = 1
a = 0, b = 1 => a+b => 0+1 => 1
a = 1, b = 1 => a+b => 1+1 => 2
a = 1, b = 2 => a+b => 1+2 => 3
a = 2, b = 3 => a+b => 2+3 => 5
a = 3, b = 5 => a+b => 3+5 => 8
a = 5, b = 8 => a+b => 5+8 => 13
a = 8, b = 13 => a+b => 8+13 => 21
a = 13, b = 21 => a+b => 13+21 => 34
a = 21, b = 34 => a+b => 21+34 => 55
a = 34, b = 55 => a+b => 34+55 => 89
a = 55, b = 89 => a+b => 55+89 => 144

"""