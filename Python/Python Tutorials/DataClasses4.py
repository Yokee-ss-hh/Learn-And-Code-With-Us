from dataclasses import dataclass , field
# Inheritance in data classes

print("********* Base class and derived classes are dataclasses ***********")

'''
@dataclass
class Animal:

    name : str
    gives_milk : bool
    mammal : bool


@dataclass
class Cow(Animal):

    specs : str


cow = Cow('short and beautiful')
animal = Animal('jaour',True,True)


print(cow.specs)
print(cow.name)
print(cow.gives_milk)
print(cow.mammal)
'''

# According to inheritance in normal concrete classes this should print the values we passed in the
# constructor right ?
# In normal classes, __init__ of class Cow overrides the __init__ of class Animal, so that both classes can
# initialize the variables on their own.
# Objects of derived class can access the data of the base class.

# BUT , In dataclasses internal init of derived class will not override the init of the base class
# and in the derived class object creation we need to pass the data for the base class variables as well
# The variables values should start from the base class variables until the derived class variables.


@dataclass
class Animal:

    name : str
    gives_milk : bool
    mammal : bool


@dataclass
class Cow(Animal):

    specs : str


cow = Cow('jaour',True,True,'short and beautiful')

print(cow.specs)
print(cow.name)
print(cow.gives_milk)
print(cow.mammal)

# In order to make cow object access the base class variables, dataclass is forcing us to initialize
# Animal()'s variables that are bound to the cow object. If we want to access Animal()'s variables
# without cow object but with Animal()'s object. we want to create one, and pass 3 variables so that
# these 3 variables we pass will now bounds to Animal()'s object.

animal = Animal('mikki',False,False)

print(animal.name)
print(animal.gives_milk)
print(animal.mammal)


# NOTE : The variables are scanned from top to bottom, so remember to provide by considering
# the first variable in base class until the last variable in the derived class while creating the
# derived class object.

@dataclass
class StudyTonight:
    name: str
    type_of_website: str
    no_of_characters: str


@dataclass
class PythonStudyTonight(StudyTonight):
    name: str
    languages_covered: str


new_instance = PythonStudyTonight("Studytonight","Technical",12,"Python, C, C++")
print(new_instance)

# As i said, dataclasses scans variables starting from the baseclass and continues to derived class
# So, for the 'name' variable present in both classes, we can consider the 1 'name' that is in base class
# as both names are considering for the same object that is for the derived class object.

'''
The above is what happens when the init method is not explicitly specified in the subclass.

But your next question could be, what if the init method is specifically defined in the subclass?

In such cases, the defined init method should have the ability to initialze 
its class attributes as well as the superclass's attributes. 
Also, the order of initializing the class attributes doesn't matter.
'''


@dataclass
class StudyTonight1:
    name: str
    type_of_website: str
    no_of_characters: str


@dataclass(init = False)
class PythonStudyTonight1(StudyTonight1):
    name: str
    languages_covered: str

    def __init__(self, type_of_website):
        self.type_of_website = type_of_website
        self.name = "Studytonight"
        self.languages_covered = "Python, C, C++"
        self.no_of_characters = 12


new_instance1 = PythonStudyTonight1("Studytonight")
print(new_instance1)


# Dataclasses Inheritance works weird, when all variables of base class has default values

'''
@dataclass
class Position:
    name: str
    lon: float = 0.0
    lat: float = 0.0


@dataclass
class Capital(Position):
    country: str  # Does NOT work
'''

# This code will immediately crash with a TypeError complaining that “non-default argument ‘country’ follows
# default argument.” The problem is that our new country field has no default value,
# while the lon and lat fields have default values.
# The data class will try to write an .__init__() method with the following signature:

# def __init__(name: str, lon: float = 0.0, lat: float = 0.0, country: str):
#     ...

# However, this is not valid Python. If a parameter has a default value,
# all following parameters must also have a default value. In other words,
# if a field in a base class has a default value, then all new fields added in a subclass must
# have default values as well.
#
# Another thing to be aware of is how fields are ordered in a subclass.
# Starting with the base class, fields are ordered in the order in which they are first defined.
# If a field is redefined in a subclass, its order does not change.
# For example, if you define Position and Capital as follows:


@dataclass
class Position:
    name: str
    lon: float = 0.0
    lat: float = 0.0


@dataclass
class Capital(Position):
    country: str = 'Unknown'
    lat: float = 40.0


# Then the order of the fields in Capital will still be name, lon, lat, country.
# However, the default value of lat will be 40.0.

capital = Capital('Madrid', country='Spain')
print(capital)

print("*****************************************************************************************")

