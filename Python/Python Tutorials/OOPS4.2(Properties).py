print("*****************************************************************************************")
print("************* Properties In Python **********************")

# Signature of property : property(fget=None, fset=None, fdel=None, doc=None)
print(type(property()))
print(property())
print(property().getter)
print(property().setter)
print(property().deleter)
print(property().fget)
print(property().fset)
print(property().fdel)

print("********** Example 1 **************")


class Circle:
    def __init__(self, radius):
        self._radius = radius

    def _get_radius(self):
        print("Get radius")
        return self._radius

    def _set_radius(self, value):
        print("Set radius")
        self._radius = value

    def _del_radius(self):
        print("Delete radius")
        del self._radius

    radius = property(
        fget=_get_radius,
        fset=_set_radius,
        fdel=_del_radius,
        doc="The radius property."
    )


circle = Circle(10)
print(circle.radius)
circle.radius = 20
print(circle.radius)
del circle.radius  # deletes the value in the radius property
try:
    print(circle.radius)
except Exception as exception:
    print(exception)

circle.radius = 50

print(circle.radius)


print("********** Example 2 **************")


class Employee:

    def __init__(self):

        self.name = None

    def getter_func(self):

        return self.name

    def setter_func(self,value):

        self.name = value

    def deleter_func(self):

        del self.name

    emp_prop = property()
    emp_prop = emp_prop.getter(getter_func)
    emp_prop = emp_prop.setter(setter_func)
    emp_prop = emp_prop.deleter(deleter_func)

    print(emp_prop.fget is getter_func)
    print(emp_prop.fset is setter_func)
    print(emp_prop.fdel is deleter_func)


employee = Employee()
employee.emp_prop = 'yokesh'
print(employee.emp_prop)


print("********** Example 3 **************")
# setting and getting multiple values using iterables.


class Student:

    def __init__(self,a,b):

        self.fname = a
        self.lname = b

    def get_values(self):

        return (self.fname , self.lname)

    def set_values(self,args):

        self.fname = args[0]
        self.lname = args[1]

    stu_prop = property(get_values,set_values)


students = Student('yokesh','chowdary')
print(students.stu_prop)
students.stu_prop = ('blade','babji')
print(students.stu_prop)


print("********** Example 4 *************")
# getter and setter using decorators
# getter function should have @property on it
# setter function should have @<getter_name>.setter on it
# deleter function should have @<getter_name>.deleter on it

'''
def get_x(self):
  return self._x
  
x = property(get_x)

is equivalent to

@property
def get_x(self):
  return self._x
'''


class FourWheels:

    def __init__(self,shape,color):

        self.wheel_shape = shape
        self.car_color = color

    @property
    def get_car_color(self):

        return self.car_color

    @property
    def get_wheel_shape(self):

        return self.wheel_shape

    @get_car_color.setter
    def set_car_color(self,x):

        self.car_color = x

    @get_wheel_shape.setter
    def set_wheel_shape(self,y):

        self.wheel_shape = y


car = FourWheels('round','red')
print(car.get_car_color,car.get_wheel_shape)

car.set_car_color = 'yellow'
car.set_wheel_shape = 'eclipse'

print(car.get_car_color,car.get_wheel_shape)

# In the above example, without using 2 getters and 2 setters , we can use list,tuple so that using only
# 1 getter and 1 setter we can get and set any number of values in a class

print("********** Example 5 *************")
# Why property let's discuss in detail

#  let’s create a Person class that contains the first, last and fullname of the
#  person as attributes and has an email() method that provides the person’s email.


class Person():

    def __init__(self, firstname, lastname):
        self.first = firstname
        self.last = lastname
        self.fullname = self.first + ' '+ self.last

    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)


# Create a Person object
person = Person('selva', 'prabhakaran')
print(person.first)  #> selva
print(person.last)  #> prabhakaran
print(person.fullname)  #> selva prabhakaran
print(person.email())  #> selva.prabhakaran@email.com

# Now, somehow you decide to change the last name of the person.
#
# Here is a fun fact about python classes: If you change the value of an attribute inside a class,
# the other attributes that are derived from the attribute you just changed don’t automatically update.
#
# For example: By changing the self.last name you might expect the self.full attribute,
# which is derived from self.last to update. But unexpectedly it doesn’t.
# This can provide potentially misleading information about the person.
#
# However, notice the email() works as intended, even-though it is derived from self.last

# Changing the `last` name does not change `self.full` name, but email() works
person.last = 'prasanna'
print(person.last)  #> prasanna
print(person.fullname)  #> selva prabhakaran
print(person.email())  #> selva.prasanna@email.com

# So, a probable solution would be to convert the self.fullname attribute to a fullname() method,
# so it will provide correct value like the email() method did. Let’s do it.

print("*******************************************")


class Person1():

    def __init__(self, firstname1, lastname1):
        self.first1 = firstname1
        self.last1 = lastname1

    def fullname1(self):
        return self.first1 + ' '+ self.last1

    def email1(self):
        return '{}.{}@email.com'.format(self.first1, self.last1)


person1 = Person1('selva', 'prabhakaran')
print(person1.fullname1())  #> selva prabhakaran

# change last name to Prasanna
person1.last1 = 'prasanna'

print(person1.fullname1())  #> selva prasanna

# Now the convert to method solution works.

# But there is a problem.
#
# Since we are using person.fullname() method with a '()' instead of person.fullname as attribute,
# it will break whatever code that used the self.fullname attribute.
# If you are building a product/tool, the chances are, other developers and users of your module used
# it at some point and all their code will break as well.
#
# So a better solution (without breaking your user’s code) is to convert the method as a
# property by adding a @property decorator before the method’s definition. By doing this,
#
# the fullname() method can be accessed as an attribute instead of as a method with '()'.
# See example below.

print("*******************************************")


class Person2():

    def __init__(self, firstname2, lastname2):
        self.first2 = firstname2
        self.last2 = lastname2

    @property
    def fullname2(self):
        return self.first2 + ' '+ self.last2

    def email2(self):
        return '{}.{}@email.com'.format(self.first2, self.last2)


# Init a Person
person2 = Person2('selva', 'prabhakaran')
print(person2.fullname2)  #> selva prabhakaran

# Change last name to Prasanna
person2.last2 = 'prasanna'

# Print fullname
print(person2.fullname2)  # selva prasanna

# Now you are able to access the fullname like an attribute.
#
# However there is one final problem.
#
# Your users are going to want to change the fullname property at some point.
# And by setting it, they expect it will change the values of the first and
# last names from which fullname was derived in the first place.
#
# But unfortunately, trying to set the value of fullname throws an AttributeError.

try :

    person2.fullname2 = 'raja rajan'

except Exception as eee:

    print(eee)

# How to tackle this?
#
# We define an equivalent setter method that will be called everytime a user sets a value to this property.
#
# Inside this setter method, you can modify the values of variables that should
# be changed when the value of fullname is set/changed.
#
# However, there are a couple of conventions you need to follow when defining a setter method:
#
# The setter method should have the same name as the equivalent method that @property decorates.
# It accepts as argument the value that user sets to the property.
# Finally,you need to add a @{methodname}.setter decorator just before the method definition.
#
# Once you add the @{methodname}.setter decorator to it, this method will
# be called everytime the property (fullname in this case) is set or changed. See below.

print("*******************************************")


class Person3():

    def __init__(self, firstname3, lastname3):
        self.first3 = firstname3
        self.last3 = lastname3

    @property
    def fullname3(self):
        return self.first3 + ' '+ self.last3

    @fullname3.setter
    def fullname3(self, name3):
        firstname3, lastname3 = name3.split()
        self.first3 = firstname3
        self.last3 = lastname3

    def email3(self):
        return '{}.{}@email.com'.format(self.first3, self.last3)


# Init a Person
person3 = Person3('selva', 'prabhakaran')
print(person3.fullname3)  #> selva prabhakaran
print(person3.first3)  #> selva
print(person3.last3)  #> prabhakaran

# Setting fullname calls the setter method and updates person.first and person.last
person3.fullname3 = 'velu pillai'

# Print the changed values of `first` and `last`
print(person3.fullname3) #> velu pillai
print(person3.first3)  #> velu
print(person3.last3)  #> pillai

# There you go. We set a new value to person.fullname, the person.first and person.last updated as well.
# Our Person class will now automatically update
# the derived attributes (property) when one of the base attribute changes and vice versa.

# Similar to the setter, the deleter’s method defines what happens when a property is deleted.
#
# You can create the deleter method by defining a method of the same
# name and adding a @{methodname}.deleter decorator. See the implementation below.

print("*******************************************")


class Person4():

    def __init__(self, firstname4, lastname4):
        self.first4 = firstname4
        self.last4 = lastname4

    @property
    def fullname4(self):
        return self.first4 + ' ' + self.last4

    @fullname4.setter
    def fullname4(self, name4):
        firstname4, lastname4 = name4.split()
        self.first4 = firstname4
        self.last4 = lastname4

    @fullname4.deleter
    def fullname4(self):
        self.first4 = None
        self.last4 = None

    def email4(self):
        return '{}.{}@email.com'.format(self.first4, self.last4)


# Init a Person
person4 = Person4('selva', 'prabhakaran')
print(person4.fullname4)  # > selva prabhakaran

# Deleting fullname calls the deleter method, which erases self.first and self.last
del person4.fullname4

# Print the changed values of `first` and `last`
print(person4.first4)  # > None
print(person4.last4)  # > None

# In above case, the person.first and person.last attribute return None, once the fullname is deleted.
print("********************************************************************************************")

# properties is used to make private variables to access outside the class


class PrivateVars:

    def __init__(self):

        self.__k = None

    @property
    def get_x(self):

        return self.__x

    @get_x.setter
    def set_x(self,value):

        self.__x = value


pv = PrivateVars()

pv.set_x = 23
print(pv.get_x)

# Using property we initialized private variable with value from outside the class and
# accessed that private variable to outside of the class and printed it.

print("***************************************************************************************")



