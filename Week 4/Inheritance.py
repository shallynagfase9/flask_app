# When one class is inheriting the properties of another class that is something we called as Inheritance.
class parent:
    def test_parent(self):
        print("This is my Parent class")

class child(parent):
    pass
child_obj = child()
print(child_obj.test_parent())


###################################
# Multilevel Inheritance
class class1:
    def test_class1(self):
        print("This is my class")

class class2(class1):
    def test_class2(self):
        print("This is my class2")

class class3(class2):
    def test_class3(self):
        print("This is my class3")

class3_obj = class3()
print(class3_obj.test_class1())
print(class3_obj.test_class3())
print(class3_obj.test_class2())

# Multiple Inheritance
class class1:
    def test_class1(self):
        print("This is my class")

class class2:
    def test_class2(self):
        print("This is my class2")

class class3(class1, class2):
    pass

class3_obj = class3()
print(class3_obj.test_class1())
print(class3_obj.test_class2())



