# An exception is an event, which occurs during the execution of a program that
# disrupts the normal flow of the program's instructions.
# In general, when a Python script encounters a situation that it cannot cope with,
# it raises an exception.
# An exception is a Python object that represents an error.

'''
The try block lets you test a block of code for errors.
The except block lets you handle the error.
The else block lets you execute code when there is no error.
The finally block lets you execute code, regardless of the result of the try- and except blocks.
'''


try:

    print(22 / 0)

except ZeroDivisionError as e1:

    print(e1)

else:

    print("I will execute only if there is no error")

finally:

    print("I will execute all times")


# In except: if i don't know the exception name, you can use Exception keyword like,
# except Exception as <some name>:

try:
    name = 'yokesh'
    if len(name) == 6:

        raise ValueError("Length should be greater than 10")

except Exception as e3:

    print(e3)

# You can use except ValueError if you knew that ValueError is raised in try block

'''
1) Exception : Base class for all exceptions
2) StopIteration : Raised when next() method of iterator finds no element in the iterable
3) SystemExit : Raised by sys.exit() method from sys module
4) ArithmeticError : Base class for all arithmetic errors
5) FloatingPointError : Raised when floating point calculation fails
6) ZeroDivisionError : Raised when divison/modulo operation takes place with zero at denominator
7) AssertionError : Raised by assert statement failure
8) AttributeError : Raised by attribute reference/attribute assignment failure
                    x = 20
                    print(x.append(30)) raises attribute error
9) ImportError : When import statement fails
10) EOFError : When end of file is reached and still we are asking for data then it raises
11) KeyBoardInterrupt : When user interrupts code execution
12) IndexError : When the index is not found in the sequence
13) KeyError : When specified key is not found in the dictionary
14) NameError : When a variable/identifier is not found in the global/local scope of the code
                print(x) but x is not defined in the code, then name error
15) UnboundLocalError : When you try to access a local variable inside a function
                        but no value has been assigned to it
16) IOError : When you try to open a file that does not exist
17) SyntaxError : Syntax is incorrect
18) IndentationError : Indentation is not matching in the code/ in correct indentation
19) SystemError : When interpreter finds an internal problem. Generally raised when python interpreter
                  does not exit.
20) TypeError : Raised when an operation/function is attempted that is invalid for that datatype
21) ValueError : Raised when the built-in function for a data type has the valid type of arguments, 
                 but the arguments have invalid values specified.
22) RunTimeError : Raised when the error does not fall into any exception category.
23) NotImplementedError : Raised when an abstract method that needs to be implemented in an 
                          inherited class is not actually implemented.
'''


# Custom Exceptions in python
'''In Python, users can define custom exceptions by creating a new class. 
This exception class has to be derived, either directly or indirectly,from the built-in Exception class. 
Most of the built-in exceptions are also derived from this class.
'''


class InvalidHeightException(Exception):

    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return repr(self.msg)


inp = int(input("Enter a number between 1 to 10:"))

try:
    if type(inp) != int or inp not in list(range(3,8)):

        raise InvalidHeightException("Height should be in between 3 and 7 feet")

except InvalidHeightException as e:

    print(e.msg)

    # print(e) also gives the same output


# https://stackoverflow.com/questions/67497900/how-the-as-keyword-works-in-exception-handling
# Look in the above link for understanding of 'as' keyword usage in python exceptions

print("***************************************************************************************")

# raise from in exceptions
# Source 1: https://www.pythontutorial.net/python-oop/python-raise-from/
# Source 2 : https://stackoverflow.com/questions/24752395/python-raise-from-usage







