# init function is used to pass the data inside the class.
# By using double underscore ( __ ) you're hiding your code from the users, as a creator of the code only you can have access to the code.
# users can access the code by certain methods.
# Encapsulation is a way to restrict the direct access to some components of an object, so users cannot access state values for all of the variables of a particular object.
# Encapsulation can be used to hide both data members and data functions or methods associated with an instantiated class or object.
class car:
    def __init__(self, year, make, model, speed):
        self.__year = year
        self.__make = make
        self.__model = model
        self.__speed = 0
    def set_speed(self, speed):
        self.__speed = 0 if speed<0 else speed
    def get_speed(self):
        return self.__speed
    
obj_car = car("2023","toyota","innova",12)
obj_car._car__year=2024
print(obj_car._car__year)
print(obj_car.get_speed())
obj_car.set_speed(3784)
print(obj_car.get_speed())

# Banking 
class bank_account:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance = self.__balance + amount

    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance = self.__balance - amount
            return True
        else:
            return False
    def get_balance(self):
        return self.__balance
    
obj_bank_account = bank_account(1000)
print(obj_bank_account.get_balance())

obj_bank_account.deposit(6000)
print(obj_bank_account.get_balance())

obj_bank_account.withdraw(4000)
print(obj_bank_account.get_balance())

