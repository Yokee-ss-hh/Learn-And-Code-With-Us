

# Access Specifiers        same class      same package    sub/derived class     other packages   other classes
# -------------------------------------------------------------------------------------------------------------
# public(default)            YES      |      YES         |        YES           |       YES      |    YES

# private                    YES      |       NO         |         NO           |        NO      |    NO

# protected                  YES      |       YES        |         YES          |        NO      |    NO


print("**************** Access Specifiers In A Class *******************")
print("**************** Encapsulation *******************")


class Employee:

    company_name = 'YokYokee'    # public class variable
    __company_area = 'TPT'       # private class variable
    _company_worth = '100Billion'  # protected class variable

    def __init__(self,lname,fname,age):
        self.lname = lname       # public instance variable
        self.__fname = fname     # private instance variable
        self._age = age          # protected instance variable

    def i_will_call_private_instance_variable(self):

        return self.__fname

    def _i_will_also_call_private_instance_variable(self):

        return self.__fname

    @classmethod
    def i_will_call_private_class_variable(cls):

        return cls.__company_area

    @classmethod
    def _i_will_also_call_private_class_variable(cls):

        return cls.__company_area

    def i_will_print_all_public_protected_class_and_instance_variables(self):

        print(self.lname, self._age, self.__fname)
        print(self.company_name,self._company_worth,self.__company_area)

    def _i_will_also_print_all_public_protected_class_and_instance_variables(self):

        print(self.lname, self._age, self.__fname)
        print(self.company_name, self._company_worth, self.__company_area)

    @classmethod
    def i_will_print_all_public_protected_class_variables(cls):

        print(cls.company_name, cls._company_worth, cls.__company_area)

    @classmethod
    def _i_will_also_print_all_public_protected_class_variables(cls):

        print(cls.company_name, cls._company_worth, cls.__company_area)

    def public_method1(self):

        self.__private_method1()

    def _protected_method1(self):

        self.__private_method1()

    def __private_method1(self):

        print(self.__fname)
        print(self.__company_area)

    @classmethod
    def public_method2(cls):
        cls.__private_method2()

    @classmethod
    def _protected_method2(cls):
        cls.__private_method2()

    @classmethod
    def __private_method2(cls):
        print(cls.__company_area)


emp = Employee('oh','yes','23')

print(f"public class variable accessed using Employee class name : {Employee.company_name}")
print(f"protected class variable accessed using Employee class name : {Employee._company_worth}")
try:
    print(f"private class variable accessed using Employee class name : {Employee.__company_area}")
except Exception as e :
    print(e)

print(f"public instance variable accessed using Employee class object emp : {emp.lname}")
print(f"protected instance variable accessed using Employee class object emp : {emp._age}")
try:
    print(f"private instance variable accessed using Employee class object emp : {emp.__fname}")
except Exception as e1:
    print(e1)

# As, We saw that private class and instance variables cannot be accessed outside the class
# So, Use public/protected methods to access private variables and calling using object.

# calling public method of class Employee to get private instance variable of the object emp
print(f"private instance variable of object emp called using public method by "
      f"object emp is : {emp.i_will_call_private_instance_variable()}")

print(f"private instance variable of object emp called using protected method by "
      f"object emp is : {emp._i_will_also_call_private_instance_variable()}")

# We can also access private instance variable outside the class using name mangling technique

print(f"private instance variable of object emp called using name mangling technique by the"
      f"object emp is : {emp._Employee__fname}")


# Now, We have accessed all types of variables in the class outside with some techniques
# except, private class variable.

# We can use class method to get access outside the class


print(f"private class variable of the class Employee accessed "
      f"via public class method using class name is : {Employee.i_will_call_private_class_variable()}")

print(f"private class variable of the class Employee accessed "
      f"via protected class method using class name is : {Employee._i_will_also_call_private_class_variable()}")


print(f"private class variable of the class Employee accessed "
      f"via public class method using object name is : {emp.i_will_call_private_class_variable()}")


print(f"private class variable of the class Employee accessed "
      f"via protected class method using class name is : {emp._i_will_also_call_private_class_variable()}")


# We can access public and protected class,instance variables using public,protected methods
# Let's see,

emp.i_will_print_all_public_protected_class_and_instance_variables()
emp._i_will_also_print_all_public_protected_class_and_instance_variables()

Employee.i_will_print_all_public_protected_class_variables()
Employee._i_will_also_print_all_public_protected_class_variables()


# We have successfully accessed all private,public and protected variables outside the class using dot operator
# and using methods also.

'''
Final Notes : 
1) public and protected instance variables,methods can be accessed using object and dot operator
2) public and protected class variables,methods can be accessed using class name,dot operator and instance,dot operator
3) private class and instance variables are accessible inside class only
4) If we want to access private variables outside of the class, we need to specify private class variables and instance
   variables inside a public/protected methods and to call these methods from outside the class.
5) second method to access private class variables outside of the class is to use class methods and calling these 
   class methods using class name or using object name with dot operator
'''
# Let's use public / protected methods to call private instance method and private class,instance variables
# outside the class using object and dot operator.
# As, private methods cannot be called outside the class, we can call private methods inside public/protected methods.
# Inside private methods, we can return / print private,class instance variables, so that private variables can access-
# - outside the class too.

emp.public_method1()
emp._protected_method1()


# Similarly, we can access private class methods and private class variables outside the class using
# public / protected class methods .

emp.public_method2()
emp._protected_method2()

Employee.public_method2()
Employee._protected_method2()


print("****************************************************************************************")
# We saw that we can access private,public and protected variables outside the class.
# But, Can we modify/change private,protected and public variables from outside the class.
# Let's see !!!!!!


class Pubg:

    def __init__(self,gun,level,car):

        self.gun_name = gun
        self._game_level = level
        self.__car_name = car

    def access_private_variable(self):

        return self.__car_name

    def change_private_variable(self,some_value):

        self.__car_name = some_value

    def _access_private_variable(self):

        return self.__car_name

    def _change_private_variable(self, some_value):

        self.__car_name = some_value


pubg = Pubg('akm',60,'dacia')

# We can access public and protected variables directly using object and dot operator

print("Initially Pubg class public variable is : ",pubg.gun_name)
print("Initially Pubg class protected variable is :",pubg._game_level)

pubg.gun_name = 'm416'
pubg._game_level = 75

print("After changing Pubg class public variable is : ",pubg.gun_name)
print("After changing Pubg class protected variable is :",pubg._game_level)

# But, we cannot access private variable directly using object and dot operator
# We need to use either public/protected methods to change or access it.

print("Initially Pubg class private variable is : ",pubg.access_private_variable())

pubg.change_private_variable('UAZ') # changing private variable using public method

print("After changing Pubg class private variable using public method is : ",pubg.access_private_variable())

pubg._change_private_variable('Open jeep') # changing private variable using protected method

print("After changing Pubg class private variable using protected method is : ",pubg._access_private_variable())

print("***************************************************************************************")
