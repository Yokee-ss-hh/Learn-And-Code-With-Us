print("************ Hybrid Inheritance *************")
# Diamond pattern
# Hybrid Inheritance = Hierarchical Inheritance(first half) + Multiple Inheritance(second half)
'''
                A
                |
           -------------
           |           |
           B           C
           |           |
           -------------
                |
                D
As class D inherits from both classes 'B' and 'C', If these 2 classes has same 
methods then duplicates are formed in class 'D'.
In the below example output we can find that Class1 is printed twice because of this duplicate methods 
in multiple inheritance
we can avoid this behavior and can access 1 method in multiple inheritance using super() function that is 
implemented by MRO internally.This pattern we can see in Example2
'''
print("***Example1 ***")
print("**********method repetition in multiple inheritance while using Class names "
      "to call base class methods *****************")


class Class1:
    def m(self):
        print("In Class1")


class Class2(Class1):
    def m(self):
        print("In Class2")
        Class1.m(self)


class Class3(Class1):
    def m(self):
        print("In Class3")
        Class1.m(self)


class Class4(Class2, Class3):
    def m(self):
        print("In Class4")
        Class2.m(self)
        Class3.m(self)


obj = Class4()
obj.m()

'''
The output of the above code has one problem associated with it, the method m of Class1 is called twice. 
This happens because, when we call base class methods using class names, python won't use MRO technique.
So, it contains duplicates.
In order to remove these repetitions of methods/code especially in multiple inheritance, we need to use-
-super() method that uses MRO technique that removes duplication internally.
Python provides a solution to the above problem with the help of the super() function.
'''

print("***Example2 ***")
print("**********Removing method repetition in multiple inheritance using super() that uses MRO"
      "internally *****************")


class Class5:
    def m1(self):
        print("In Class5")


class Class6(Class5):
    def m1(self):
        print("In Class6")
        super().m1()


class Class7(Class5):
    def m1(self):
        print("In Class7")
        super().m1()


class Class8(Class6, Class7):
    def m1(self):
        print("In Class8")
        super().m1()


obj1 = Class8()
obj1.m1()

print("**************** From stackoverflow super() working order on methods *******************")


class FooBase(object):
    def foo(self):
        print('FooBase.foo()')


class A(FooBase):
    def foo(self):
        print('A.foo() before super()')
        super().foo()
        print('A.foo() after super()')


class B(FooBase):
    def foo(self):
        print('B.foo() before super()')
        super().foo()
        print('B.foo() after super()')


class C(A, B):
    def foo(self):
        print('C.foo() before super()')
        super().foo()
        print('C.foo() after super()')


c = C()
c.foo()

print(C.__mro__)
'''
MRO calculating manually:
BEFORE : C -> A -> FooBase -> Object -> B -> FooBase -> Object
AFTER : Remove duplicates from right to left 
Final MRO : C -> A -> B -> FooBase -> Object
'''
'''
1) c.foo() asks python to search for foo() in class 'C', it successfully finds it and prints line 97
2) As soon as it encounters line 98, control goes to line 82 and prints line 83
3) Now control goes to line 84, there it finds the super() that asks python to go to line 77 in class 'FooBase'
4) But according to mro graph in line 110, methods in FooBase should not print until methods in class 'B' executes
5) So, control goes to line 89 and prints line 90 .Now, control goes to line 90 and python finds the 
   method in FooBase .Now python sees in mro graph that all methods in the classes before class FooBase has 
   executed as of now. So,python executes line 78 and prints it.
6) Later line 92 in class 'B' prints, then line 85 in class 'A' prints , finally line 99 in class 'C' prints
'''
print("*************************************************************************")


# Creating a Base class named University:
class University:

    def __init__(self):
        print("Constructor of the Base class")
        # Initializing a class variable named univ to store university name:
        self.univ = "MIT"

    def display(self):  # Method to print the University Name:
            print(f"The University name is: {self.univ}")


# 1st Derived or Child Class of University Class:
class Course(University):

    def __init__(self):

        # using "super" keyword to access members of the parent class having same name:
        print("Constructor of the Child Class 1 of Class University")
        University.__init__(self)
        self.course = "CSE"

    def display(self):  # Method to print the Course Name:

        # using "super" keyword to access display method defined in the parent class:
        print(f"The Course name is: {self.course}")
        University.display(self)


# 2nd Derived or Child Class of University Class:
class Branch(University):

    def __init__(self):
        print("Constructor of the Child Class 2 of Class University")
        self.branch = "Data Science"

    def display(self):  # Method to print the Branch Name:

        print(f"The Branch name is: {self.branch}")


# Derived or Child Class of Class Course and Branch:
class Student(Course, Branch):

    def __init__(self):

        print("Constructor of Child class of Course and Branch is called")
        self.name = "Tonny"
        Branch.__init__(self)
        Course.__init__(self)

    def display(self):

        print(f"The Name of the student is: {self.name}")
        Branch.display(self)
        Course.display(self)


# Object Instantiation:
ob = Student()  # Object named ob of the class Student.
print()
ob.display()  # Calling the display method of Student class.

print("*************************************************************************")

print(issubclass(Course,University))
print(issubclass(Branch,University))
print(issubclass(Student,Course))
print(issubclass(Student,Branch))

print(isinstance(ob,Student))
print(isinstance(ob,Course))
print(isinstance(ob,Branch))
print(isinstance(ob,University))