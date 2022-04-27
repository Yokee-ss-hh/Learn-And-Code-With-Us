# In Python, We have None datatype that is an object of class NoneType
#
# This class is a singleton, meaning that there can be only one instance of it.
#
# In fact, all the variables assigned to none, point to the same object in Python and all these variables have same
# memory location.
#
# None datatype implicitly evaluates to False .
my_variable = None
print(type(my_variable))

# As , We know there is always one instance of the class 'NoneType'. All objects storing the 'None' value points
# to the same memory address. Let's check whether it is True/False.

print("**********************************************************")
var1 = None
var2 = None
var3 = None

print(id(None))
print(id(var1))
print(id(var2))
print(id(var3))
# In the output we will get same memory address for all those 3 variables as well as for 'None' Type.

print('***********************************************************')
# Let's check using '==' and identity(is) operators.
print(var1 == None)
print(var2 == var1)
print(var2 == var3)

print("***********")
print(var1 is var2)
print(var2 is var3)
print(var3 is var1)

print("***********")
# We can use None in conditional statements as well,
if(not None):
    print("Hello There!")

if(None):
    print("This line never executes!")
else:
    print("Something prints now")

print("*************")
# Boolean check to None,
print(bool(None))
print(not bool(None))

print("***********************")
# The function calls that is not returning anything gives None.
def some_func():
    print("I am printing............")
return_store = some_func()
print(return_store)
print(type(return_store))
print(id(return_store))

print("******************************")
# Note : Look at the different id's we printed in different examples! We have the same memory address . That means
# how many times we use 'None' at different parts and scenarios of the program, all are pointing to the same memory
# address only.
