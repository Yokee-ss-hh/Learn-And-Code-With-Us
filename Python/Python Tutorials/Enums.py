import enum


class Animal(enum.Enum):

    legs = 2
    animal_type = "mammal"

print(Animal)
print(type(Animal))

print(Animal.legs)
print(type(Animal.legs))

print(Animal.animal_type)
print(type(Animal.animal_type))

print(Animal.legs.value)
print(Animal.animal_type.value)

# Using For Loop

for x in Animal:

    print(x)

for y in Animal:

    print(y.value)

# enums can be accessed using name and value as,

# accessing using values
print(Animal(2))
print(Animal('mammal'))

# accessing using names
print(Animal['legs'])
print(Animal['animal_type'])

print(Animal.animal_type.name)
print(Animal.legs.name)

# Assigning Animal Variables to another variables like aliasing,

variable1 = Animal.legs
variable2 = Animal.animal_type

print(variable1.name, ":", variable1.value)
print(variable2.name, ":", variable2.value)

# Can use repr() on enums as

print(repr(Animal.legs))
print(repr(Animal.animal_type))

print("***********************************************************************************")


class Season(enum.Enum):
    SPRING = 1
    SUMMER = 2
    AUTUMN = 3
    WINTER = 4


seas = Season.SPRING
print(seas == Season.SPRING)

print(list(Season))

print(isinstance(seas,Season))

for item in Season:

    print(item.name, item.value)

print("************************************************************************************")

Foods = enum.Enum('Foods', ['biryani','Dal','Egg Rice','Sambar'],)

# start = 1 by default

print(Foods.biryani.value)

# We can change start to any other number also,

SeaFoods = enum.Enum('SeaFoods', ['fish','crab','lobster'], start = 10)

print(SeaFoods.fish.value)

print("************************************************************************************")
# Python enum values can be automatically set with the auto function.

Transport = enum.Enum('Transport',[('BUS',10),('TRAIN',20),('AIRPLANE',30)])

for x in Transport:

    print(x.name, x.value)

# can use __members__

for x,y in Transport.__members__.items():

    print(x,y.value)

print("************************************************************************************")

# Can enum variables be duplicates ?
# enum member names should be unique, if not python raises TypeError
# enum memner values can be same, python won't raise any error, but while printing
# using for loop it takes first appearance members only , Look below


class Color(enum.Enum):

    YELLOW = 2
    BLACK = 2
    WHITE = 3
    PURPLE = 4
    ORANGE = 5


for g in Color:

    print(g.name,g.value)


# If i try to print the duplicate valued 'BLACK' explicitly using print statement,
# I will get the original valued member i.e, YELLOW

print(Color.BLACK.name, Color.BLACK.value)

# This happens because , YELLOW was initialized with 2 value first, then BLACK is initialized with 2.
# So, Even if we call BLACK , it considers BLACK.
# This is the weird behavior in enums


print("************************************************************************************")

# We can make all member names and their values unique using @unique decorator

# In the above example 2 different members of enum class has same value
# Both YELLOW and BLACK has same value 2 in them.
# But, python did not raised error and it ignored 'BLACK' while trying to print using for loop
# Even, if i tried to print manually like in line 132, it replaced BLACK with YELLOW and gave output

# WE can make all members and their values unique at the time of writing enum classes
# using @enum.unique decorator

try:
    @enum.unique
    class School(enum.Enum):
        a = 1
        b = 2
        c = 2

except ValueError as e:

    print(e)

print("************************************************************************************")

# The enum.Flag is a base class for creating enumerated constants
# that can be combined using the bitwise operations without losing their Flag membership.


class Perm(enum.Flag):
    EXECUTE = enum.auto()
    WRITE = enum.auto()
    READ = enum.auto()


print(list(Perm))
print(Perm.READ | Perm.WRITE)

print("************************************************************************************")
# enum.Enum vs enum.INTEnum vs enum.STREnum

# Normal enum stores all datatypes
# Comparing members of normal enums gives false


class Colors1(enum.Enum):

    RED = 1
    BLUE = 'blue'


class Colors2(enum.Enum):

    RED = 1
    BLUE = 'blue'


print(Colors1.RED == 1)
print(Colors1.BLUE == 'blue')


print(Colors1.RED == Colors2.RED)
print(Colors1.BLUE == Colors2.BLUE)

print("*****************************************")

# enum.INTEnum makes the class should have only integers as the values to their members
# Comparing members with the values gives True , but in normal enums gives False

try:

    class Even(enum.IntEnum):

        EVEN_ONE = 2
        EVEN_TWO = 'four'

except Exception as e:

    print(e)


# So, only integers should be members of enum.INTEnum


class Evens1(enum.IntEnum):

        EVEN_ONE = 2
        EVEN_TWO = 4


class Evens2(enum.IntEnum):
    EVEN_ONE = 2
    EVEN_TWO = 4


print(Evens1.EVEN_ONE == 2)
print(Evens2.EVEN_ONE == 2)
print(Evens1.EVEN_ONE == Evens2.EVEN_ONE)

print("*******************************************************************************")
# There is no support for enum.STREnum for python 3.10 , In 3.11 update we have
# enum.STREnum
# enum.STREnum works same like a enum.INTEnum

# IT only accepts string values to it's members
# Raises error if non-string values are initialized to enum members
# enum.STREnum python docs : https://docs.python.org/3.11/library/enum.html#enum.StrEnum


























