# functions use def keyword
print("*******************************************************************************************")
print("*****Different types of functions*****")


def return_nothing(): # returns nothing
    print("hi")


def return_something(): # returns something
    return 22


def fn_with_parameters(x,y):
    return x+y


def fn_with_default_args(f_name = 'yokesh',l_name = 'chowdary'):
    return f_name+l_name

# Note : IF a function has both default and normal parameters, then
# default parameters should follow normal parameters
# like fn(a,b,c,d=20) not fn(a=10,b,c,d) if we do so we will get error


def fn_with_both_default_and_normal_params(a,b,c=10):
    return a+b+c

def fn_with_if(x):
    if x % 2 == 0:
        return "Even Number"
    return "Odd Number"


def fn_returns_list(some_list):
    for _ in range(len(some_list)):
        some_list[_] = chr(some_list[_])
    return some_list


def fn_returns_tuple():
    return 10,20,30      # comma separated by multiple values are treated as tuple


return_nothing()
print(return_something())
print(fn_with_parameters(21,31))
print(fn_with_default_args())       # this function uses default args
print(fn_with_default_args('yoki','yokee')) # this function uses user input args
print(fn_with_if(9))
print(fn_with_if(10))
print(fn_returns_list([69,70,71,72,73]))
print(fn_returns_tuple())
print(fn_with_both_default_and_normal_params(20,30))

print("*******************************************************************************************")
# In function definition, the arguments should maintain this format,
# def some_fn(a,b,c,d......,*args1,*args2,.......,*kwargs1,**kwargs2,........):
print("***** args and kwargs *****")
# *args --> positional arguments
# *kwargs --> keyword arguments


def fn_without_args1(a,b,c):
    print(a+b+c)


def fn_without_args2(a,b,c):
    print(a+b+c)


def fn_with_args1(a,b,c,d,e):
    print(a+b+c+d+e)


def fn_with_args2(*params):
    print(params)


def fn_with_args3(p1,p2,*p3):  # should follow order arg1,arg2,....,*argN
    print(p1,end=",")
    print(p2,end=",")
    print(p3)


fn_without_args1(11,22,33)      # arguments order should match with parameters
fn_without_args2(b=20,c=10,a=22)   # arguments order is not mandatory, as we specified parameters names -
# -function call arguments.
fn_with_args1(1,3,5,7,9)
fn_with_args2(2,4,6,8,10)
fn_with_args3(3,6,9,12,15,18,21)


def fn_without_kwargs1(fname,lname,age):
    print(f"{fname} {lname} is {age} years old!....")


def fn_without_kwargs2(lname,age,fname):
    print(f"{fname} {lname} is {age} years old!....")


def fn_with_kwargs1(**leaders):
    print(leaders)


def fn_with_kwargs2(x, **z):
    print(x,end=",")
    print(z)


fn_without_kwargs1('yokesh','chowdary',22)  # The order of arguments is important and -
# - should match with order of parameters.

fn_without_kwargs1(fname='yokesh',lname='chowdary',age=22)  # The order of arguments is not important-
# - as we specified parameters names in function call arguments.

fn_with_kwargs1(india_leader = "modi",russia_leader = 'putin',usa_leader = 'biden')

fn_with_kwargs2(21,fname="valar",lname="morghulis")


def fn_with_args_and_kwargs(x,y,z,*a,**b):
    print(x,end=",")
    print(y,end=",")
    print(z,end=",")
    print(a,end=",")
    print(b,end="")


fn_with_args_and_kwargs(1,2,3,4,5,6,7,one='1',two='2',three='3')


print("*********************************************************************************")


def some_function(*args):

    y = args
    return y


print(some_function([1,2,3,4,5]))
print(some_function((1,2,3,45)))


print('\n')

print("*********************************************************************************")
print("************** Pass by value, pass by reference and pass by assignment *********************")

# 1) Python’s argument passing model is neither “Pass by Value” nor “Pass by Reference”-
# -but it is “Pass by assignment”.

# According to python docs,
# Remember that arguments are passed by assignment in Python-
# -Since assignment just creates references to object, there’s no-
# -alias between an argument name in the caller and callee, and so no call-by-reference .

# What exactly python docs telling is,
# 1) The parameter passed in is actually a reference to an object (but the reference is passed by value).
# 2) Some data types are mutable, but others aren't.(immutable)

# If you pass a mutable object into a method, the method gets a reference to that same object
# ,and you can mutate it to your heart's delight,
# but if you rebind the reference in the method, the outer scope will know nothing about it,
# and after you're done, the outer reference will still point at the original object.


# If you pass an immutable object to a method, you still can't rebind the outer reference,
# and you can't even mutate the object as even changing a single thing in immutable objects
# creates entirely new object in the memory, The best example is string.

a = 'yokesh'
print(f"before changing a : {a}, {id(a)}")
a = 'hello'
print(f"After changing a : {a}, {id(a)}")

b = [1,2,3]
print(f"before changing b : {b}, {id(b)}")
b = [3,4,5]
print(f"after changing b : {b}, {id(b)}")

'''
From above 2 examples, mutable and immutable objects upon modifying it's contents completely with new contents-
- always creates new  addresses in the memory.
mutable objects upon adding/deleting a single item from them is reflected back in the original mutable object.
immutable objects upon adding/deleting it's contents will create a new object in the memory with that changes.
'''

print("********************************************************")
print("*********** pass by reference Example 1 for mutable data types ************")


def try_to_change_list_contents(the_list):
    print('got', the_list)
    the_list.append('four')
    print('changed to', the_list)


outer_list1 = ['one', 'two', 'three']

print('before, outer_list =', outer_list1)
try_to_change_list_contents(outer_list1)
print('after, outer_list =', outer_list1)

# Explanation by Yokesh :
# Here, We just modified the outer_list by adding one more item to it. So it will hold back-
# - it's reference to outside the function.
# So, python treats this as "pass by reference".

# Explanation in Stackoverflow :
# Since the parameter passed in is a reference to outer_list, not a copy of it,
# we can use the mutating list methods to change it and have the changes reflected in the outer scope.

print("********* pass by value Example 2 for mutable data types ************")


def try_to_change_list_reference(the_list):
    print('got', the_list)
    the_list = ['and', 'we', 'can', 'not', 'lie']
    print('set to', the_list)


outer_list2 = ['we', 'like', 'proper', 'English']

print('before, outer_list =', outer_list2)
try_to_change_list_reference(outer_list2)
print('after, outer_list =', outer_list2)

# Explanation by Yokesh :
# Here We entirely erased the list contents of outer_list2 and re-assigned with new values.
# So, python creates entirely new object with re-assigned contents and re allocates-
# -that new object to new variable named "the_list".
# So, python treat this process as "pass by value" as references are broken inside the function.

# Explanation in Stackoverflow :
# Since the the_list parameter was passed by value, assigning a new list to it had no effect that the-
# -code outside the method could see. The the_list was a copy of the outer_list reference, and-
# -we had the_list point to a new list, but there was no way to change where outer_list pointed.


print("*********** Example 3 for mutable data types **************")

# In example 2, We discussed pass by value to a function, and the inner changes made in that function-
# - is not reflecting outside the function, Can we reflect those new changes made inside the function to-
# - outside????

# Yes, we can


def try_to_change_entire_list_contents_inside_a_function_and_making_reference_to_outer_list3(the_list):
    print('got', the_list)
    the_list = ['and', 'we', 'can', 'not', 'lie']
    print('set to', the_list)
    return the_list


outer_list3 = ['we', 'like', 'proper', 'English']

print('before, outer_list =', outer_list3, id(outer_list3))

outer_list3 = try_to_change_entire_list_contents_inside_a_function_and_making_reference_to_outer_list3(outer_list3)

print('after, outer_list =', outer_list3, id(outer_list3))

# The Id's of outer_list3 before and after the function call is not same, because at line 246, the reference to-
# -the function outer3 is broken with the function. After returning the new list at line 255 and assigning -
# - it to outer_list-3 creates new object in the memory and names it outer_list3.
# After this naming, line 251 is deleted permanently in the memory.


print("*********** pass by value Example 4 for immutable data types **************")


def try_to_change_string_reference(the_string):
    print('got', the_string)
    the_string = 'In a kingdom by the sea'
    print('set to', the_string)


outer_string1 = 'It was many and many a year ago'

print('before, outer_string =', outer_string1)
try_to_change_string_reference(outer_string1)
print('after, outer_string =', outer_string1)

# Again, since the the_string parameter was passed by value, assigning a new string to it-
# -had no effect that the code outside the method could see. The the_string was a copy of the-
# -outer_string reference, and we had the_string point to a new string, but there was no way -
# -to change where outer_string pointed.

print("*********** pass by value Example 4 for immutable data types **************")

# In the above example, python created a new string named 'the_string' when we changed the -
# - content of the passed string.
# Thus, creating entirely 2 string objects with 2 different contents.
# But, I want the changed string inside the function with the same name as outer_string,
# How can i do this?????


def try_to_change_string_reference_with_original_name(the_string):
    print('got', the_string)
    the_string = 'In a kingdom by the sea'
    print('set to', the_string)
    return the_string


outer_string2 = 'It was many and many a year ago'
print('before changing, outer_string =', outer_string2, id(outer_string2))
outer_string2 = try_to_change_string_reference_with_original_name(outer_string2)
print('after changing, outer_string =', outer_string2, id(outer_string2))

# Initially outer_string2 is pointing to 'It was many and many a year ago' object in the memory.
# After the function returned 'In a kingdom by the sea' object which has a new memory address, python-
# - simply breaks the outer_string2 connection to  'It was many and many a year ago' object and make-
# - outer_string2 points to new object with value 'In a kingdom by the sea'.
# The object "'It was many and many a year ago'" will be cleaned by garbage collector as it's reference-#
# - count is dropped to zero.

print("************** Another Example **************")


def use_a_wrapper_to_simulate_pass_by_reference(stuff_to_change):
    new_string = (lambda x : x[0] + 'yokesh')(stuff_to_change)
    stuff_to_change[0] = new_string

# then you could call it like


wrapper = ['He is the one who was called king in the north : ']
use_a_wrapper_to_simulate_pass_by_reference(wrapper)
print(wrapper[0])


print("********************************************************************************")
print("*********************************************************")
print("***** multiple return statements : *****")

def multiple_returns(num):

    if num > 3 and num < 5:

         return 'OK'

    elif num > 5 and num < 10:

        return 'hello'

    return 'hi' # This acts as else block


print(multiple_returns(num:=int(input('Enter num :'))))

# num = 10, o/p = hi
# num = 7 , o/p = hello
# num = 4, o.p = ok
