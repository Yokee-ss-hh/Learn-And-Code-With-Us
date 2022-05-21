print("********* Python Variable Scopes and Inner Functions ************")
print("*****************************Example 1*********************************")
var1 = "I am global variable!.." # global variable 1
# global variables are accessed everywhere in the program.


def f1():
    print(f"The global variable var1 that is accessed inside a function f1() is : {var1}")


f1()
print("******************************Example 2*********************************")

# Local variable with the same name as global variable.


def f2():
    var1 = "I am local variable"
    print(f"I am the local variable var1 that has the same name as global variable"
          f" created locally inside f2 function that has value : {var1}")


f2()
print(f"I am global variable var1 accessed outside the function f2 which is having local variable "
      f"name same as the global variable : {var1}")

# Modifying global variable inside a local function gives error

print("***********************Example 3********************************************")

name = "yokesh" # global variable 2


def f3():
    global name
    name = name+"chowdary"
    print(f"Global variable name modified inside the function f3 using global keyword is : {name}")


f3()

print("*****************************Example 4****************************************")
# function accessing both local and global variables

country = "india" # global variable 3


def f4():
    global country
    continent = 'asia' # local to f4
    country = country*2
    print(f"Global variable country modified and printed inside f4 is : {country}")
    print(f'Local variable continent created inside f4 is : {continent}')


f4()


print("********************************************************************************")
print("****** Inner Functions *******")

# global variables can be accessed in outer and inner functions also.
language = 'python' # global variable 4


def outer1():
    print(f"global variable langauge accessed inside the outer function outer1 is : {language}")

    def inner1():
        print(f"global variable language accessed inside the inner function inner1 "
              f"belonging to the outer function outer1 is : {language}")

    inner1()


outer1()

print("************************************************************************")
# variables of outer f'n can be accessed by inner fn's.
def outer2():
    outer_variable1 = 99

    print(f"Outer variable inside the outer function outer2 is : {outer_variable1}")

    def inner2():
        inner_variable1 = 29

        print(f"Inner variable inside the inner function inner2 of outer function outer2 is : {inner_variable1}")
        print(f"Outer variable inside the inner function inner2 of outer function outer2 is : {outer_variable1}")

    inner2()


outer2()


# Let's see whether we can modify the global variable in both outer and inner functions.

fav_fruit = 'mango' # global variable 5


print("************************************************************************")
def outer3():
    global fav_fruit
    print('global variable fav_fruit before modifying is : ',fav_fruit)
    fav_fruit = 'apple'
    print(f"global variable fav_fruit after modifying inside the outer function outer3 is : {fav_fruit}")
    def inner3():
        global fav_fruit

        fav_fruit = 'kiwi'
        print(f"global variable fav_fruit after modifying in the inner function inner3 of outer function"
              f"outer3 is : {fav_fruit}")

    inner3()


outer3()


print("************************************************************************")


def some_outer():
    x = 20 # global variable for some_inner() function
    print(f"x inside some_outer function is : {x} ")

    def some_inner():
        global x
        x = 40
        print(f"x is modified inside inner function of some_outer function : {x}")
    some_inner()
    print(f"x inside some_outer function after modifying : {x}")


some_outer()

# From the lines 126 to 135, we saw that outer function variable cannot be modified inside the
# inner function even using the global variable, so we need to use nonlocal keyword.
print("************************************************************************")
# outer function variables cannot be modified inside the inner functions
# so, we need to use non-local keyword.
# How nonlocal keyword works ?
'''
some_global_variable = '....'
fn1{
    name = "....."
    fn2{
        name = ".........."
        fn3{
            name = "...."    # Let, inner function variable called as 'name'
        }
    }

}
'''
'''
1) nonlocal keyword binds one or more variables in the inner function to the variables with the-
- same name in it's outer scope functions.
2) if the immediate outer scope has no matching 'name', it goes to the next outer scope.
3) if none of the outer scopes have same variable 'name' ,we will get error(line 260 to 286)-
-means, nonlocal keyword variable name in the inner function should match with atleast one variable -
-in it's outer functions.
4)Assume the program execution is at the inner most scope ('n' levels inside from a function call), -
-the global keyword makes the 'name'  to be directly bound to global scope,-
-while the nonlocal keyword makes the name to be bound to next outer scope at which the name is available.
5) Inner Function accessing variable from outer function scope is called as non local scope.
6) In the immediate example below, inner4 function accessing/modifying outer4 function's variable-
- outer_variable2 from nonlocal scope.
'''


print('**************************************************************************')


def outer4():
    outer_variable2 = 'best'
    print('Outer variable of outer4 function before modifying is : ',outer_variable2)

    def inner4():
        nonlocal outer_variable2
        outer_variable2 = outer_variable2 + ' juice'
        print('Outer function variable outer_variable2 after modifying in inner function inner4 '
              'using nonlocal keyword is ',outer_variable2)
    inner4()
    print(outer_variable2)


outer4()

print("**************************************************************************")
# nonlocal example 1 :

val = 0



def f1():
    val = 5

    def f2():
        val = 7.5

        def f3():
            nonlocal val

            val = 10
            print("f3:", val)

        f3()

        print("f2:", val)

    f2()

    print("f1:", val)

f1()

'''
Explanation of output:
1) As soon as python encounters nonlocal keyword in line 177, it immediately checks for the variable named-
- 'val' in it's outer scope. It will see that 'val' is present at line number 174.
2) So, python changes that variable value in the outer f2() function to 10. That means the variable 'val'
has value of 10 in both f2 and f3 functions.
3) But,The value of 'val' in the functions f1 and the global variable has 5 and 0 respectively.
'''

print("*************************************************************************************")
val1 = 0


def f11():
    val1 = 5

    def f21():

        def f31():
            nonlocal val1

            val1 = 10
            print("f31:", val1)

        f31()

        print("f21:", val1)

    f21()

    print("f11:", val1)


f11()
'''
After python encounters nonlocal keyword on line 212,it checks for the variable val1 in the -
-immediate outer scope of it i.e, in f21(). But in f21() python encounters nothing with the name of 'val1'.
So, it checks for the variable with name 'val1' in the next outer scope i.e, in f11(), there it finds -
- the variable with name 'val1', so it modifies the variable 'val1' in f11() with the initialized variable-
- value of 'val1 = 10' which is in the f31().
So, all the functions with the variable name of 'val1' has value as 10, and global variable is untouched as we found -
- variable 'val1' in the f11() itself, so global variable 'val1' is untouched and has value of 0 only.
'''

print("******************************************************************************")
'''
val2 = 0


def f12():

    def f22():

        def f32():
            nonlocal val2

            val2 = 10
            print("f32:", val2)

        f32()

        print("f22:", val2)

    f22()

    print("f12:", val2)


f12()

Error : SyntaxError: no binding for nonlocal 'val2' found
'''

print("***************************************************************************************")
'''
y = 10


def ff():
    print("ff : ",y)

    def ff1():
        print("ff1 :",y)

        def ff2():
            print("ff2 :",y)

            def ff3():
                nonlocal y
                y = 20

            ff3()
        ff2()
    ff1()

    
ff()

Error : SyntaxError : no binding for nonlocal 'y' found
'''
