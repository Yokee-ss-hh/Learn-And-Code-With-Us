'''
instance methods  vs  class methods  vs  static methods
'''

print("*************** Instance Method in a class ****************")
print('\n')


class Employee:

    company_type = 'Private'

    # creates instance variables using __init__
    def __init__(self,area_code,area_name):

        self.area_code = area_code

        self.area_name = area_name

    # creates instance variables using instance method
    def instance_method(self,state):

        self.state_name = state

    # instance method to print the objects data
    def show_employee_details(self):

        print(f"Employee {self} works in a {self.__class__.__name__} company that is located in {self.area_name}, "
              f"{self.area_code} in {self.state_name}")

    def modify_area_name(self,x):

        self.area_name = x


# 1st way to create instance variables using constructor
yokesh = Employee(12345,'khushinagar')
# 2nd way to create instance variables using instance method
yokesh.instance_method("AP")
yokesh.show_employee_details()

# 3rd way to create instance variables using setattr() method
setattr(yokesh,'age',23)
print("yokesh age :",yokesh.age)

# 4th way to create instance variables is
yokesh.city = 'pakala'
print('yokesh lives in :',yokesh.city)

yokesh1 = Employee(87654,'Gopalpur')
yokesh1.instance_method("KNTKA")
yokesh1.show_employee_details()
setattr(yokesh1,'age','24')
print("yokesh1 age : ",yokesh1.age)
yokesh1.city = 'tirupati'
print('yokesh1 lives in :',yokesh1.city)

# So, Until now we created 2 objects
# 2 instance variables using constructor (lines 40,53)
# 1 instance variables using dot operator by direct initialization (line 50,58)
# 1 instance variable using setattr() (line 46,56)
# 1 instance variable using instance method (line 42,54)

# Can instance of a class modify / create a class variable ???

# Changing class variable using objects will not create impact on class variable directly
print(f"class variable company_type before modifying : {yokesh.company_type}")
print(f"class variable company_type before modifying : {Employee.company_type}")

yokesh.company_type = 'Ocean1'

print(f"class variable company_type before modifying : {yokesh.company_type}")
print(f"class variable company_type before modifying : {Employee.company_type}")

# So, class variable accessed by object yokesh will return Ocean1 only,
# Remaining all objects other than yokesh will return Private only

print(f"class variable company_type of object yokesh 1 gives : {yokesh1.company_type}")

# That means , if class variables are modified using object name and dot operator,it will not create
# impact at class level and on other objects.

# As you can see modifying class variable using object will not impact on original class variable
# Then How to change class variable using object that originally creates impact on class variable ???
# Use , object_name,__class__.class_variable_name


print(f"class variable company_type before modifying : {yokesh.company_type}")
print(f"class variable company_type before modifying : {Employee.company_type}")


yokesh.__class__.company_type = 'Public'

print(f"class variable after modifying : {yokesh.company_type}")
print(f"class variable after modifying : {Employee.company_type}")


# Even with this process we cannot modify the class variable.

# So, Using class name only we can do the change as ,

Employee.company_type = 'Public'

print(yokesh.company_type) # returns Ocean1 as we modified it in the above statements
print(yokesh1.company_type)
print(Employee.company_type)


# We can modify / delete the existing instance variables using instance methods.
yokesh.modify_area_name('kmpalli')
print(f"area_name after modification : {yokesh.area_name}")


# We can delete the instance variables using del keyword and delattr() method

del yokesh1.area_name

delattr(yokesh1,'area_code')

try:
    print(yokesh1.area_name)

except Exception as e1:
    print(e1)

try:
    print(yokesh1.area_code)

except Exception as e2:
    print(e2)


# Things to remember :
'''
1) instance variables can be modified using constructor, instance method, using dot operator, using setattr() 
2) class variables can be accessed by using both objects  and class names
3) changes made to class variables using object is upto the object itself and not reflect at class level
4) changes made to class variables using class name will reflect at class level and all it's objects.
5) instance variables are accessed using object name only.
6) instance methods can be called by object name only.
'''
# All proofs to the above 5 points are in example class Employee
print('\n')


print("*************** Class Method in a class ****************")
# Using classmethod() and @classmethod decorator

'''
1) Class methods are methods that are called on the class itself, not on a specific object instance. 
   Therefore, it belongs to a class level, and all class instances share a class method.
2) A class method is bound to the class and not the object of the class. It can access only class variables
3) It can modify the class state by changing the value of a class variable 
   that would apply across all the class objects.
4) Class methods are used when we are dealing with factory methods. Factory methods are those methods that return a 
   class object for different use cases. Thus, factory methods create concrete implementations of a common interface.
'''

# Modifying class variable content using classmethod() and @classmethod
# and calling these in 3 ways
# calling classmethod decorator using classname
# calling clasmethod decorator using classname()
# passing classname.classmethod to classmethod() and returning classmethod
# calling decorator classmethod and normal classmethod() using objects of a class


class ABCD:

     city = 'Bnglr'
     food = 'biryani'
     state = 'KRNTA'

     @classmethod
     def change_class_variable_city(cls,name):
         print(f"Before modifying value of class variable is : {cls.city}")
         cls.city = name
         print(f"After modifying value of class variable is : {cls.city}")

     @classmethod
     def change_class_variable_food(cls, name):
         print(f"Before modifying value of class variable is : {cls.food}")
         cls.food = name
         print(f"After modifying value of class variable is : {cls.food}")

     def change_class_variable_state(cls,name):
         print(f"Before modifying value of class variable is : {cls.state}")
         cls.state = name
         print(f"After modifying value of class variable is : {cls.state}")

     def change_class_variable_city_temporary(cls):
         cls.city = 'kanpur'


# calling class method decorator using class name
ABCD.change_class_variable_city('HYD')

# calling class method decorator using class name()
ABCD().change_class_variable_food('Haleem')

# using classmethod() method
ABCD.change_class_variable_state = classmethod(ABCD.change_class_variable_state)
ABCD.change_class_variable_state('tlngna')


# Creating new objects for a class dynamically using @classmethod and classmethod()
class FactoryClasses:

    def __init__(self,lname,fname):
        self.lname = lname
        self.fname = fname

    @classmethod
    def create_new_object(cls,x,y):

        new_object = cls(x,y)
        return new_object

    def create_another_new_object(cls,a,b):

        another_new_object = cls(a,b)
        return another_new_object


fc1 = FactoryClasses.create_new_object('yokesh','chowdary')
print(fc1.fname+" "+fc1.lname)
print(isinstance(fc1,FactoryClasses))

FactoryClasses.create_another_new_object = classmethod(FactoryClasses.create_another_new_object)
fc2 = FactoryClasses.create_new_object('albert','einstein')
print(fc2.fname+" "+fc2.lname)
print(isinstance(fc2,FactoryClasses))


'''
1) In the ABCD example, we saw that how to change/modify the class variables using @classmethod
   and classmethod()
2) In the FactoryClasses example, we saw how to create new objects for a class dynamcially
   using @classmethod decorator and classmethod()
'''

# As i said earlier, we can call class methods using class instance also


class Pubg:

    game_mode = 'multiplayer'

    def __init__(self,gun):
        self.fav_gun = gun

    @classmethod
    def something_method(cls):

        cls.game_mode = 'sooperrrrrr'


pubg = Pubg('akm')
print(f"Before modifying : {Pubg.game_mode}")
pubg.something_method()
print(f"After modifying : {Pubg.game_mode}")

'''
Final Note:
1) Generally by default all methods in a class are instance methods and they bound to 
the objects of that class
2) Using classmethod() or @classmethod we can change those instance methods to class methods
3) instance methods have access to both class and instance variables
4) class methods have access to only class variables only
5) instance methods can modify instance variables permanently and class variables temporarily
6) instance methods should call with object itself
7) class methods can be called with both class name and it's objects name
'''
'''
Features  |   Class Methods   |     Instance Methods
--------------------------------------------------------------   
Binding	  :   Class	               An instance of the class
Calling	  :   Class.method()	   object.method()
Accessing :   Class attributes	   Instance & class attributes
'''
print("\n")

print("*************** Static Method in a class ****************")

# constructing static method using staticmethod() and @staticmethod decorator

'''
A static method is a general utility method that performs a task in isolation. Inside this method, 
we don’t use instance or class variable because this static method doesn’t take any parameters like self and cls.
'''
'''
1) A static method does not receive an implicit first argument like self , cls
2) A static method is also a method that is bound to the class and not the object of the class.
3) A static method can’t access or modify the class state.
4) It is present in a class because it makes sense for the method to be present in class.
5) We generally use class method to create factory methods. 
   Factory methods return class objects ( similar to a constructor ) for different use cases.
   We generally use static methods to create utility functions.
6) static methods cannot modify class variables and instance variables.
'''


class StaticExample:

    @staticmethod
    def sample1():

        print("Hi i am sample method1")

    def sample2():

        print("Hi i am sample method2")

    @staticmethod
    def sample3():

        print("Hi i am sample method3")


StaticExample.sample1() # or StaticExample().sample1()

StaticExample.sample2 = staticmethod(StaticExample.sample2)
StaticExample.sample2() # or StaticExample().sample2()

sample_object = StaticExample()
sample_object.sample3()

# In the above example,
# We created a static method using @staticmethod decorator and staticmethod()
# We called static method using class-name(with and without brackets) and using object.


# static method using along with the instance method
class Employ():

    def __init__(self, name, salary, project_name):
        self.name = name
        self.salary = salary
        self.project_name = project_name

    @staticmethod
    def gather_requirement(project_name):
        if project_name == 'ABC Project':
            requirement = ['task_1', 'task_2', 'task_3']
        else:
            requirement = ['task_1']
        return requirement

    # instance method
    def work(self):
        # call static method from instance method
        requirement = self.gather_requirement(self.project_name)
        for task in requirement:
            print('Completed', task)


kelly = Employ('Kelly', 12000, 'ABC Project')
jessa = Employ('Jessa', 7000, 'XYZ Project')

# false
# because seperate copy of instance method is created for each object
print(kelly.work is jessa.work)

# True
# because only one copy is created
# kelly and jess objects share the same methods
print(kelly.gather_requirement is jessa.gather_requirement)

# True
print(kelly.gather_requirement is Employ.gather_requirement)


# Calling methods in chain pattern
class Test :
    @staticmethod
    def static_method_1():
        print('static method 1')

    @staticmethod
    def static_method_2() :
        Test.static_method_1()

    @classmethod
    def class_method_1(cls) :
        cls.static_method_2()


# call class method
Test.class_method_1()


# Calling static method inside instance method
class InsideOutside:

    def in1(self):
        temp = self.in2()
        print(temp)

    @staticmethod
    def in2():
        return 20


insideout_obj = InsideOutside()
insideout_obj.in1()

print('\n')

print("Static methods inside the class should call with either class name or object name")
print("methods outside the class are completely static as no class method and no instance methods"
      "present outside the class, so methods outside the class can be called directly like function()")

print("*******************************************************************************")
print("********* Final Note : ***********")
'''
  class method                          instance method                           static method
-----------------------------------------------------------------------------------------------------
Only access to class variables       Can access both class and instance             Cannot access class and 
                                     variables                                      instance variables
                                
Can be called using both class       Can be called using instance name only         Can be called using both class,
and objects name                                                                    objects names. 

Can modify class variable            Can modify it's instance variables             Cannot modify either class or 
                                                                                    instance variables
                                                                                    
Cannot modify all of it's            Can modify it's class variables temp-           """""""""""""""""""""""""""
instance variables                   -orarily only.If this object is deleted,
                                     we cannot see the changes we made to that 
                                     object    
                                     
@classmethod and classmethod()        No special methods as by default every        @staticmethod and staticmethod()    
is used here                          method is instance method                     is used here

class method also called factory      No special name for instance method           static method also called utility 
methods as class methods can                                                        functions
return a new object
'''

print("******************************************************************************************")
