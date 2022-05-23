print("*** First class objects, Closures and Decorators ***")

'''
First class objects can be stored in any datastructure that python allows like int,float,dict..etc etc.
Functions are first class objects in python.
Functions can be stored in lists,tuples,dicts,sets etc etc , stored in variables also.
Functions can be aliased with another name.
Functions can be passed as arguments to another Functions.
Functions can be returned by another Functions.
We can pass functions as another function arguments, return a function in another function and assign a function-
- to another variable.
The first class object plays a key role in python for decorators design.
'''
print("***************************************First Class Objects****************************************************")
print("*********aliasing a function************")


def print_something(text):
    print(f"The text is : {text}")


aliased_print_something = print_something

aliased_print_something('Yokesh')
print_something('hello there!...')

print("**************Passing one function to another as argument*****************")


def milk_shake(mixer, water, milk):
    return mixer(water, milk)


def mixer(water, milk):
    print('mixing water and milk.........')
    return water + milk


print(f"The prepared litres of MilkShake is : {milk_shake(mixer, 10, 20)}")


def add_two_nums(x, y):
    return x + y


def add_three_nums(sum_func, x, y, z):
    return sum_func(x, y) + z


print(add_three_nums(add_two_nums, 2, 3, 4))

print("**********************Returning a function from another function***************************")


def outer():
    def inner():
        return 23

    return inner


x = outer()

print(x())

print("********************* storing functions in lists ********************************")


def f1():
    return 'hi'


def f2():
    return 'hello'


def f3():
    return 'how are you'


def f4():
    return 'yokesh'


functions_list = [f1, f2, f3, f4]

for function in functions_list:
    print(function(), end=" ")
print('\n')
print("************************ storing functions in dictionary ******************************")

functions_dicts = {'f1': lambda x: x + 2, 'f2': lambda y: y + 3, 'f3': lambda z: z + 4}

dicts_list = list(functions_dicts.values())

print(dicts_list[0](2))
print(dicts_list[1](4))
print(dicts_list[2](6))

print('\n')

print("******************* storing function type variables *************************")


def func_variables(fname, lname, age):
    func_variables.fname = fname
    func_variables.lname = lname
    func_variables.age = age


func_variables('yokesh', 'chowdary', 22)
print(func_variables.fname)
print(func_variables.lname)
print(func_variables.age)

# As every function is an object, we can store variables of that function type.
# The above program is the example for that.

print("*****************************************************************************************")
print("********** Closures *************")
print(" A Closure is a nested function that references one or more variables from its enclosing scope.")
# As closures are used as callback functions, they provide some sort of data hiding.
# This helps us to reduce the use of global variables.

'''
def say():
    greeting = 'Hello'   | ->
                         |
    def display():       |          These lines from 111 to 116 is called as closure.
        print(greeting)  |
                         |
    display()            | -> 
'''
'''
1) display() is called as nested function, and getting a free variable from its nonlocal scope
2) Here python treats greeting variable as free variable
3) When we examine display() function, we can observe 2 things , One is the display() function-
- is nested inside the say() function ,second is the greeting variable which is a free variable.
4) The combination of that display() function accessing free variable greeting from it's nonlocal scope-
- is called as Closure.
'''


# In python outer function can return inner function as ,


def say():
    greeting = 'Hello Yokesh'

    def display():
        print(F'I Belongs To Inner Function display() : {greeting}')

    return display


returned_say = say()
returned_say()

'''
1) The say() function is executed by python and it's returned inner function display() is stored in-
- returned_say variable.
2) When returned_say() function executes, the execution of say() function already completed.
3) That means, the scope of say() function was gone at the time when returned_say() executes.
4) Since, greeting variable belongs to say() function, it should also be destroyed along with its-
- say() function.
5) BUT, Even though greeting variable is in out of scope-
 -greeting variable is accessed by the alias of display() i.e, returned_say() .
6) How this happens ?
'''

# The Working Of Closures !

'''
1) The value of the greeting variable is shared in 2 scopes , namely say() function and the closure.
2) Even though the name of the variable is accessed in 2 different scopes, but they are implicitly-
- pointing to the same memory address where it's value "Hello Yokesh" is staying.
3) To achieve this, python uses intermediate object called 'cell' .
   __________________________________
   |        non local scope         |
   |        (greeting variable)--------------------|     
   |  ____________________          |              |_______
   |  |   local scope    |          |                      |----->|------------------|
   |  |                  |          |                             |      cell        |
   |  |                  |          |                             | 0x000123hdha123d |--------->"Hello Yokesh"   
   |  | greeting variable---------------------------------------->|------------------|         0x005487fde43jh21
   |  |__________________|          |
   |                                |
   |                                |
   |________________________________|
   
4) As soon as python encounters closure it immediately creates a cell object where greeting variable from 2 -
- different scopes are pointing to it. Then, cell object points to the object 'Hello Yokesh' memory address.
5) After say() function executed and it returns the display() function, the say() function and greeting variable-
- goes out of scope. But ,the returned inner function will points to the cell object where it can get value of-
- the greeting variable.
6) That's how python creates closure and returned inner function accesses the variable 'greeting'- 
-from it's outer function's nonlocal scope.
7) We can find the address of cell object using __closure__ and we can find the address of the free variable-
- the closure is accessing from it's nonlocal scope by using __code__.co_freevars.
'''
print(returned_say.__closure__)
print(returned_say.__code__.co_freevars)


# These 2 above things returns a tuple where the cell is present in the memory and where the free variable is.
# Line 184 , returns tuple with cell address where greeting variable from 2 scopes points to,
# and string address where value of free variable stores.

# Proof that greeting variable in 2 scopes points to cell object,
def say1():
    greeting1 = 'Hello'
    print("I am from outer scope pointing to cell object at :", hex(id(greeting1)))

    def display1():
        print("I am from inner scope pointing to cell object at :", hex(id(greeting1)))
        # print(greeting1)

    return display1


fn1 = say1()
fn1()

# As we see both are printing the same memory address where the cell object actually resides.

print("*********************** closure example 1 *************************")


def multiplier(x):
    def multiply(y):
        return x * y

    return multiply


m1 = multiplier(1)
m2 = multiplier(2)
m3 = multiplier(3)

print(m1(10))  # o/p : 10
print(m2(10))  # o/p : 20
print(m3(10))  # o/p : 30

print(m1.__closure__)
print(m1.__code__.co_freevars)

print(m2.__closure__)
print(m2.__code__.co_freevars)

print(m3.__closure__)
print(m3.__code__.co_freevars)

'''
Outer multiplier function has a variable 'x' and inner multiple function has 'y' variable.
For the inner multiple function, variable 'x' is nonlocal.
In the first function call to multiplier, i.e, multiplier(1), the inner function consumes 'x' and returns-
- inner function. Python identifies this as a closure and creates 2 scopes with variable 'x' ans points -
- to cell object. In turn the cell object points to value 1.
Look at line 227,228 where we can find the addresses of formed cell and the value it is pointing to.

Similarly, For the next 2 function calls i.e, multiplier(2) and multiplier(3) python creates brand new 2 -
- different cells and then those 2 cells points to 2 and 3 respectively.

So, For the above program, for 3 function calls, python creates 3 closures, 3 cells to maintain 3 values of-
- 'x' variables.

From 227 to 234 lines, we can see that 3 different cells at different memory locations was created and those 
3 cells are pointing to 3 different addresses where value of 'x' for each function call is stored.
'''
print("************************************************************************")
print("*************** Example 2 ***********************")


# Storing all closures in a list , later calling them with passing value.


def multiplier1(x1):
    def multiply1(y1):
        return x1 * y1

    return multiply1


multipliers = []  # Stores all 3 closures
for x in range(1, 4):  # creates 3 closures using value iterating from 1 to 3
    multipliers.append(multiplier1(x))

m1, m2, m3 = multipliers  # List Unpacking

print(m1(10))  # closure 1 call
print(m2(10))  # closure 2 call
print(m3(10))  # closure 3 call

print('************************************************************************')
print("**************** Example 3 *********************")


def add_num(n):
    def addition(x):
        return x + n

    return addition


add_2 = add_num(2)
add_8 = add_num(8)
print(add_2(4))
print(add_2(8))
print(add_8(add_2(7)))

print("**************************************************************************")
print("*************** Example 4 *********************")


def forest():
    animals = 200

    def population():
        return animals

    return population


amazon = forest()
print(amazon())

print('************************************************************************')
print("****************** Example 5 ***********************")


# example for changing outer methods variable in inner function closure using  nonlocal keyword.


def data_transfer(text):  # outer method

    message = text

    def data_transmission():  # nested method
        nonlocal message
        message = 'The message in the data_transfer() outer method is ' \
                  'changed by it\'s inner method data_transmission()'
        return message

    return data_transmission


nested_fun = data_transfer("Change this secret message !")
print(nested_fun())

print("***************************************************************************")
print('*********** Advantages of closures *********************')

print('During the usage of callback functions, '
      'the usage of closures helps in data hiding as well as in the reduction of '
      'usage of global variables.')

print('When the number of methods that need to be implemented inside a class is few in number, '
      'closures can be used instead, '
      'since they tend to provide a much elegant solution.')

print('The cool aspect of closure is that it allows the function data to be seen even after its execution is over')

print('Closures in python are function objects which have the ability to remember '
      'some amount of data (present in the enclosing scope) '
      'even after the execution of code is complete')

print('\n')

print("***************************************************************************")
print("************ Decorators ***************")

# A decorator takes in a function, adds some functionality and returns it

print("*********** Example 1 *************")


def i_will_add_forty(some_func):
    def i_will_also_help_to_add_forty(*args):
        variable = some_func(*args)

        variable = variable + 20

        return variable

    return i_will_also_help_to_add_forty


def my_value_will_be_forty_soon(x):
    return x


my_value_will_be_forty_soon = i_will_add_forty(my_value_will_be_forty_soon)

print(my_value_will_be_forty_soon(50))

print("*********** Example 2 **************")


# We can make Example 1 short as,

@i_will_add_forty
def my_value_will_be_forty_soon(x):
    return x


print(my_value_will_be_forty_soon(20))

print("********** Example 3 ****************")


def i_will_make_upper(func1):
    def inner1():
        x = func1()
        x1 = x.upper()
        return x1

    return inner1


def i_will_make_lower(func2):
    def inner2():
        y = func2()
        y1 = y.lower()
        return y1

    return inner2


@i_will_make_lower
def make_my_text_lower():
    return 'YOKESH'


@i_will_make_upper
def make_my_text_upper():
    return 'yokesh'


print(make_my_text_lower())
print(make_my_text_upper())

print("************ Example 4 *****************")


def i_will_add_something_about_google(function):
    def i_am_inner_function():
        print('Yokesh is saying')
        function()
        print('is the best browser')

    return i_am_inner_function


@i_will_add_something_about_google
def i_am_google():
    print('GOOGLE')


i_am_google()

print("************* Example 5 ***************")


def add_99_to_sum(some_function):
    def adding99_inner(*args):
        var_x = some_function(*args)

        var_x = var_x + 99

        return var_x

    return adding99_inner


def sum_of_two(a, b):
    return a + b


sum_of_two = add_99_to_sum(sum_of_two)

print(sum_of_two(10, 20))

print("*************************************************************************")
print("************ Decorator Chaining Example 1 **************")


def decor1(func):
    def decor1_inner():
        x = func()

        return x + 20

    return decor1_inner


def decor2(func):
    def decor2_inner():
        y = func()

        return y * 20

    return decor2_inner


@decor1
@decor2
def some_number():
    return 10


print(some_number())


# First decor2 will be performed by python.later,decor1 will be applied.
# When decor2 applied, 10*20 = 200 will be there, next when decor1 is applied, value becomes 200+20 = 220.

def that_number():
    return 10


that_number = decor1(decor2(that_number))
print(that_number())

# Both line number 524 and line number 535 gives same output.


print("************ Decorator Chaining Example 2 **************")


def remove_negative_elements(some_function):
    def inner_function1(*args):

        x = some_function(*args)

        inner_list = []

        for item in x:

            if item > 0:
                inner_list.append(item)

        return inner_list

    return inner_function1


def remove_elements_greater_than_ten(some_function):
    def inner_function2(*args):

        y = some_function(*args)

        final_list = []

        for item in y:

            if item < 10:
                final_list.append(item)

        return final_list

    return inner_function2


@remove_elements_greater_than_ten
@remove_negative_elements
def some_random_list(some_list):
    return some_list


print(some_random_list([1, 2, 3, 4, 5, -3, -4, -9, -10, 44, 321, 99, 100]))

print('\n')
print("**************************************************************************")
print("********** Lambda Functions or Anonymous Functions *************")

# A lambda function can take any number of arguments, but can only have one expression.

'''
lambda (a,b,c........n inputs) : <---single expression to handle these inputs-----> 
'''

var = lambda item: item + 20

print(var(10))  # o/p : 30

# or we can directly call lambda as,

print((lambda y: y + 20)(10))  # o/p : 30

print((lambda a, b: a + b)(1, 2))  # o/p : 3

print((lambda a, b, c: a + b + c)(1, 2, 3))  # o/p : 6

'''
The power of lambda is better shown when you use them as an anonymous function inside another function.
Say you have a function definition that takes one argument, and that argument will be multiplied with an unknown number
'''


def myfunc(n):
    return lambda a: a * n


i_will_double = myfunc(2)
print(i_will_double(5))  # o/p : 10

i_will_triple = myfunc(3)
print(i_will_triple(5))  # o/p : 15

# or we can do directly as,


def that_func(x):
    return (lambda y : x*y)(3)


print(that_func(3))    # o/p : 9

print((lambda _ : _)('yokesh'))  # o/p : yokesh

# The below line squares the list elements
print([(lambda x : x*x)(x)  for x in [1,2,3,4,5,6,7,8,9,10]]) # o/p : [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

print("*********************************************************************")


