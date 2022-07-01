# Assertions are simply boolean expressions that check if the conditions return true or not.
# If it is true, the program does nothing and moves to the next line of code.
# However, if it's false, the program stops and throws an error.
#
# It is also a debugging tool as it halts the program as soon as an error occurs and displays it.

# Syntax : assert <condition>,<error message>

'''
assert statement has a condition and if the condition is not satisfied the program 
will stop and give AssertionError.
assert statement can also have a condition and a optional error message. 
If the condition is not satisfied assert stops the program and gives AssertionError 
along with the error message.
'''

# Example of assert without a message handling using exceptions handling technique.
# As we didnt passed any default message for assert , so we provided some sentence
# in except statement.
def positive_nums(number):
    assert number > 0

    return number * 2

try:
    positive_nums(-10)

except AssertionError:

    print("Some assertion error is raised, please check functionality again")


# Example of assert with a default message handling using exceptions handling technique.
# As we passed default message for assert , so we did not provided some sentence
# in the except so that we can print the default message of assert.
def avg(marks):
    assert len(marks) != 0,"List is empty."
    return sum(marks)/len(marks)


mark2 = [55,88,78,90,79]
print("Average of mark2:",avg(mark2))

try:
      mark1 = []
      print("Average of mark1:",avg(mark1))

except AssertionError as e:

    print(e) # prints message we passed in the assert statement


# Key points:

# Assertions are the condition or boolean expression which are always supposed to be true in the code.
# assert statement takes an expression and optional message.
# assert statement is used to check types, values of argument and the output of the function.
# assert statement is used as debugging tool as it halts the program at the point where an error occurs.



