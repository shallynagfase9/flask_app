"""
A decorator is a design pattern in Python that allows a user to add new functionality to an existing object 
without modifying its structure. 
Decorators are usually called before the definition of a function you want to decorate.
"""

def deco(func):
    def inner_deco():
        print("This is the start of my fun.")
        func()
        print("This is the end of my fun.")
    return inner_deco

@deco
def test1():
    print(4+9)
print(test1())

# Write a code using Decorator function to calculate the start time and end time taken by code to execute
import time
def timer_test(func) :
    def timer_test_inner():
        start = time.time()
        func()
        end = time.time()
        print(end-start)
    return timer_test_inner
###########
@timer_test
def test1():
    print(45+67)
print(test1())

###########
@timer_test
def test2():
    for i in range(10000):
        pass
print(test2())