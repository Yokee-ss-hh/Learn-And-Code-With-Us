print("******************************************************************************")
# Walrus operator, (python 3.8.0)

'''
1) Walrus operator accomplish 2 works at a time, assigning a value to a variable and returning that value.
'''

print("***Example1***")
# Traditional way :

fruit = "mango"

print("My favorite fruit is : ",fruit)


# New way :

print("My favorite color is : ",color:="yellow")

# print("My favorite color is : ",color="yellow")
# The above line if interpreted, gives Type Error.

print("***Example2***")
# In conditional statements,

status = True
if(status):
    print("This is the old way style")

if(boolean := True):
    print("This is the new way style")


print("***Example3***")
# In Looping ,
user_name = input("Type your user name")

while(user_name != ""):
    print("Nice name bro!")
    break


while(_user_name:=input("Enter User Name:") != ""):
    print("Good Luck Guys!")
    break

# As we can see, we wrote entire logic in single line as above.

print("***Example4***")
# In List Comprehensions and function calls,
def find_area(x):
    return x*x

parameter_list = [1,2,3,4,5]

print([find_area(y) for y in parameter_list if find_area(y) < 10])

# In the above line , we are calling find_area() function twice , we can minimize it as ,

print([z for h in parameter_list if (z := find_area(h)) < 10])

# Using walrus operator , we reduced the function calls by 50%.
