'''
1) Types of constructors
2) Constructor overloading
3) Can one class have many constructors as in c++ and java ?
4) using multiple constructors in a single class with classmethod() function and using @classmethod decorator
5) creating object without __init__(self,*) in a class
6) Handling constructor overloading using *args, *kwargs and parameter data types using annotations
'''
print("*********************************************************************************************")
print("************** Overview of constructors **********************")
'''
Whenever a class is instantiated __new__ and __init__ methods are called.
__new__ method will be called when an object is created and __init__ method will be called to initialize the object. 
In the base class object, the __new__ method is defined as a static method which requires to pass a parameter cls. 
cls represents the class that is needed to be instantiated, and the compiler automatically 
provides this parameter at the time of instantiation.
'''
'''
Instance can be created inside __new__ method either by using super function or by directly calling
__new__ method over object, where if parent class is object. That is instance = super(MyClass, cls).
__new__(cls, *args, **kwargs) or instance = object.__new__(cls, *args, **kwargs)
If both __init__ method and __new__ method exists in the class, then the __new__ method is executed first 
and decides whether to use __init__ method or not, because other class constructors can be called by __new__ method
or it can simply return other objects as an instance of this class.

'''

print("******** Example1 **********")


class Point:

    def __new__(cls,*args,**kwargs):
        print ("__new__() is executing")
        print(cls)
        print(args)
        print(kwargs)
        return super().__new__(cls)
        # or we can use "return object.__new__(cls)"

    def __init__(self, x=0.0, y=0.0, z=0.0):
        print ("Instance returned by the __new__() method")
        print("Values are being initialized")
        self.mX = x
        self.mY = y
        self.mZ = z
        print("Values are initialized successfully")


p1 = Point(10,20,30)

print(p1.mX, p1.mY, p1.mZ)


# If __new__() returns no object, then __init__() cannot run on its own , Let's see

print("******** Example2 **********")


class Polygon():

    def __new__(cls, *args, **kwargs):
        print('I will not return any object because i dont want to do it ')
        return

    def __init__(self):

        print('This is __init__ method')


polygon = Polygon()
print(polygon)


# This means we can control the object creation and no: of objects creation using __new__() method.

print("******** Example3 **********")

# Both __new__() and __init__() should not have return values
# Only __new__() should return an object and that returned object is used by __init__()
# to initialize instance variables.


class Zoo:

    def __init__(self,a):
        self.a = a

        return "I am here to initialize ZOO objects variables"

try:

    Zoo_object = Zoo(21)
    print(Zoo_object)

except Exception as e :

    print(e)


print("******** Example4 **********")


class Create3objects():

    object_count = 0

    max_object_allowed = 3

    def __new__(cls, *args, **kwargs):

       if cls.object_count < cls.max_object_allowed:

            print("Your object is creating")

            cls.object_count +=1

            return super().__new__(cls)

       else:

           print("You have reached maximum limit to create a object")

    def __init__(self,name):

        self.name = name


c1 = Create3objects('object1')

c2 = Create3objects('object2')

c3 = Create3objects('object3')

c4 = Create3objects('object4')

c5 = Create3objects('object5')

# In the above example, We explicitly controlled the number of objects creation for the class Create3objects.
# So, __new__() is used to control the creation of objects.


print("******** Example4 **********")

# From above all explanations, we saw that __init__() is not the method that creates the object
# But, __new__() method creates the object, and returns it
# The returned object from the __new__() is used by __init__() to initialize that objects variables

# So, we can create a object for a class without init also


class WithoutInit:

    def obj_method(self):

        print("Hello I am this class method")


obj_without_init = WithoutInit()
obj_without_init.obj_method()

# Even, we can create and initialize this objects variables explicitly without __init__()

obj_without_init.age = 23
setattr(obj_without_init,'place','india')

print(getattr(obj_without_init,'age'))
print(getattr(obj_without_init,'place'))
# Here, we did not define a constructor, but Python instantiated that object anyway!
# This must mean it provides a default constructor that shows up when we do not provide any

print("******** Example 5 ********")


class ABCDEF:

    def __new__(cls, *args, **kwargs):

        return 40

    def __init__(self):

        self.a = 23
        self.b = 21


print(ABCDEF())

abcd = ABCDEF()

print(abcd) # This proves that ABCDEF class returned integer not it's newly created object

try:
     abcd2 = ABCDEF()
     print(abcd2.a,abcd2.b)

except AttributeError as ae:

    print(ae)

# We are getting Attribute Error because, __new__() returned 40 which is a integer
# 40 is a object which has 'int' as a class
# We returned 40 which is an object of int() class to the user defined class 'ABCDEF'
# But, __init__() in the above class ABCDEF needs object of type ABCDEF not of type int()
# So, __init__()  is not called to initialize those a,b values. That's why we are getting
# attribute error as abcd2 object do not have attributes named a,b


print("*********************************************************************************************")
print("************** Types of constructors **********************")

print("*** 1) Default Constructor ***")

# Python will provide a default constructor if no constructor is defined. Python adds a default constructor
# when we do not include the constructor in the class or forget to declare it.
# It does not perform any task but initializes the objects.
# It is an empty constructor without a body.
# If you do not implement any constructor in your class or forget to declare it, the Python inserts a
# default constructor into your code on your behalf. This constructor is known as the default constructor.
# It does not perform any task but initializes the objects. It is an empty constructor without a body.
# The default constructor is not present in the source py file.
# It is inserted into the code during compilation if not exists
# If you implement your constructor, then the default constructor will not be added.


class Default:

    def hello(self):

        print("I am default constructor and i do nothing")


default = Default()
default.hello()

# As you can see in the example, we do not have a constructor,
# but we can still create an object for the class because Python added the
# default constructor during a program compilation.


print("*** 2) Non - parameterized constructor ***")


class Company:

    # no-argument constructor
    def __init__(self):
        self.name = "PYnative"
        self.address = "ABC Street"

    # a method for printing data members
    def show(self):
        print('Name:', self.name, 'Address:', self.address)


# creating object of the class
cmp = Company()

# calling the instance method using the object
cmp.show()


print("*** 3) Parameterized constructor ***")


class Employee:
    # parameterized constructor
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    # display object
    def show(self):
        print(self.name, self.age, self.salary)


# creating object of the Employee class
emma = Employee('Emma', 23, 7500)
emma.show()

kelly = Employee('Kelly', 25, 8500)
kelly.show()


print("*** 4) Parameterized Default constructor ***")

# Parameterized Default constructor is a constructor with default values
# Python allows us to define a constructor with default values.
# The default value will be used if we do not pass arguments to the constructor
# at the time of object creation.


class Student:
    # constructor with default values age and classroom
    def __init__(self, name, age=12, classroom=7):
        self.name = name
        self.age = age
        self.classroom = classroom

    # display Student
    def show(self):
        print(self.name, self.age, self.classroom)


# creating object of the Student class
emma = Student('Emma')
emma.show()

kelly = Student('Kelly', 13)
kelly.show()


print("*********************************************************************************************")
print("************** Constructor Overloading **********************")

# There is no constructor over loading in python
# If we specify 2 or 3 constructors, python will consider the latest constructor and raises errors
# for the rest of the constructors


class MultipleConst:

    def __int__(self,a,b):

        self.a = a
        self.b = b

    def __int__(self,c=23):

        self.c = c

    def __init__(self):
        print("First Constructor")


mc1 = MultipleConst()

try :
     mc2 = MultipleConst(2,3)
except Exception as e1 :
    print(e1)
    print(e1.args)

try :
   mc3 = MultipleConst(31)

except Exception as e2:
    print(e2)
    print(e2.args)


'''
In c++/java in one class there will be 2 or more constructors with different signatures
Based on our requirements, object is created by calling one of these existing constructors
If one object is created using one constructor, another object can also be created using the same
constructor or using any of the constructors present in the class.
But in python there is no overloading , so we can implement in 3 ways 
Lets see one by one
'''
print("******* Constructor Overloading based on no: of arguments and it's types *******")


class OverloadOne:

    def __init__(self,*some_args):

        if isinstance(some_args[0],int) and isinstance(some_args[1],int):

            self.value = some_args[0] * some_args[1]

        elif isinstance(some_args[0],str) and isinstance(some_args[1],str):

            self.value = some_args[0] + some_args[1]

        else:
            self.value = str(some_args[0]) + some_args[1]


overload_obj1 = OverloadOne(10,20)

overload_obj2 = OverloadOne('yokesh','chowdary')

overload_obj3 = OverloadOne(21,'hello')

print(overload_obj1.value, overload_obj2.value,overload_obj3.value)


class Fruits:
    def __init__(self, *args, **kwargs):

       if args :

           if len(args) == 0:

               pass

           elif len(args) == 1 and isinstance(args[0],str):

               self.fruit1 = args[0]

           elif len(args) == 2 and isinstance(args[0],str) and isinstance(args[1],str):

               self.fruit1 = args[0]
               self.fruit2 = args[1]

           elif len(args) > 2:

               self.fruit1 = args[0]
               self.fruit2 = list(args[1:])

       else:

           self.fruit1 = kwargs['fav1']

           self.fruit2 = kwargs['fav2']


f1 = Fruits('apple')
f2 = Fruits('apple','banana')
f3 = Fruits('apple','banana','cherry','mango','kiwi','berry')
f4 = Fruits(fav1 = "banana",fav2 = "cherry")
print(f1.fruit1)

print(f2.fruit1,f2.fruit2)

print(f3.fruit1,f3.fruit2)

print(f4.fruit1,f4.fruit2)


print("*********** Constructor Overloading using single __init__ ****************")
'''
A class can have one constructor __init__ which can perform any action when the instance of the class is created. 
This constructor can be made to different functions that carry out different actions based on the arguments passed
'''


class OverloadTwo:

    def __init__(self,*args):

        if len(args) == 1 :

            self.final_answer = args[0]

        elif len(args) == 2 :

            self.final_answer = self.fn1(args)

        elif len(args) == 3:
            self.final_answer = self.fn2(args)

        else:
            self.final_answer = self.fn3(args)

    def fn1(self,some_args):

        return some_args[0] * some_args[1]

    def fn2(self,some_args):

        return some_args[0]*some_args[1]*some_args[2]

    def fn3(self,some_args):
        temp = 1
        for x in some_args:
            temp *=x

        return temp


oo1 = OverloadTwo(2)
oo2 = OverloadTwo(3,4)
oo3 = OverloadTwo(5,6,7)
oo4 = OverloadTwo(1,2,3,4,5,6,7,8,9,10)

print(oo1.final_answer)
print(oo2.final_answer)
print(oo3.final_answer)
print(oo4.final_answer)

print("*********** Constructor Overloading using classmethod() / @classmethod decorator ****************")

# As we know that using class method we can create objects and class variables also.

# Let's implement the above example using class methods


class OverloadThree:

    def __init__(self,*args):

        self.stored_answer = args[0]

    @classmethod
    def classmethod1(cls,*some_args):

        stored_answer = cls.funct1(some_args)

        return cls(stored_answer)

    @classmethod
    def classmethod2(cls, *some_args):

        stored_answer = cls.funct2(some_args)

        return cls(stored_answer)

    def funct1(some_args):
        return some_args[0] * some_args[1]

    def funct2(some_args):

        return some_args[0]*some_args[1]*some_args[2]


cm1 = OverloadThree(20)
print(isinstance(cm1,OverloadThree))
print(cm1.stored_answer)

cm2 = OverloadThree.classmethod1(1,2)
print(isinstance(cm2,OverloadThree))
print(cm2.stored_answer)

cm3 = OverloadThree.classmethod2(10,20,30)
print(isinstance(cm3,OverloadThree))
print(cm3.stored_answer)


# In the above example, we created 3 instances cm1,cm3 and cm3 based on the parameters
# passed to the class "OverloadThree()".
# Refer OOPS3.py file, to know more about static methods, class methods and instance methods.


print("*********************************************************************************************")






