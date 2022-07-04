import types

print(dir(types))

print(type(types) == types.ModuleType)


def some_function():

    pass


print(type(some_function) == types.FunctionType)  # some_function is a user created function

print(type(len) == types.BuiltinFunctionType)  # len is normal built-in function that can be used on anytype

some_list = [1, 2, 3, 4, 5]

print(type(some_list.append) == types.BuiltinMethodType)  # append is the built-in method of a list
                                                          # that can be used only on the list object


def generator_example():

    yield 10


x = generator_example()

print(type(x) == types.GeneratorType)  # Here x is generator object


g = lambda x : x+20

print(type(g) == types.LambdaType)   # g is referencing whole lambda

var_one = None

print(type(var_one) == types.NoneType)   # var_one is pointing to None object


def curry_go():

    return NotImplemented


print(type(curry_go()) == types.NotImplementedType) # Because curry_go upon calling returning NotImplemented
# Learn more about "NotImplemented" here : https://s16h.medium.com/pythons-notimplemented-type-2d720137bf41


# NotImplemented is one of Python’s six constants living in the built-in namespace.
# The others are False, True, None, Ellipsis and __debug__.
# Similar to Ellipsis, NotImplemented can be reassigned (shadowed).
# Assignments to it, even as an attribute name, do not raise a SyntaxError.

# NotImplemented is a special value which should be returned by the binary special methods
# (e.g. __eq__(), __lt__(), __add__(), __rsub__(), etc.) to indicate that the operation
# is not implemented with respect to the other type; it may be returned by the
# in-place binary special methods (e.g. __imul__(), __iand__()) for the same purpose.
# Also, its truth value is True:

# Let’s show the use of the NotImplemented constant by coding __eq__() for two very basic (and useless) classes A and B.
# [For this simple example, __ne__() won’t be implemented to avoid distraction,
# but in general, every time __eq__() is implemented, __ne__() should also be
# implemented unless there is a good reason for it not to be.]
class A(object):

    def __init__(self, value):
        self.value = value

    def __eq__(self, other):
        if isinstance(other, A):
            print('Comparing an A with an A')
            return other.value == self.value
        if isinstance(other, B):
            print('Comparing an A with a B')
            return other.value == self.value
        print('Could not compare A with the other class')
        return NotImplemented


class B(object):

    def __init__(self, value):
        self.value = value

    def __eq__(self, other):
        if isinstance(other, B):
            print('Comparing a B with another B')
            return other.value == self.value
        print('Could not compare B with the other class')
        return NotImplemented


a1 = A(1)
b1 = B(1)

print(a1 == a1)
print(b1 == b1)
print(a1 == b1)

# In the above 3 cases we got if conditions satisfied and booleans are returned and printed successfully

# Now, if we compare b1 with a1 (i.e. invoke b1.__eq__(a1)), we would expect NotImplemented to be returned.
# This is because B’s __eq__() only compares against other B instances. Let’s see what happens:
print(b1 == a1)

# Clever! b1.__eq__(a1) method returning NotImplemented caused A’s __eq__() method to be called and
# since a comparison between A and B was defined in A’s __eq__() then we got the correct result (True).
#
# And that is what returning NotImplemented does. NotImplemented tells the runtime that it should ask
# someone else to satisfy the operation. In the expression b1 == a1, b1.__eq__(a1) returns NotImplemented
# which tells Python to try a1.__eq__(b1). Since a1 knows enough to return True, then the expression can succeed.
# If A’s __eq__() also returned NotImplemented, then the runtime would fall back to the built-in behaviour
# for equality which is based on object identity (which in CPython, is the object’s address in memory).
#
# Note that raising a NotImplementedError when b1.__eq__(a1) fails would break out of the code unless caught,
# whereas NotImplemented doesn’t get raised and can result in/be used for further tests.


class Home:

    def home_name(self):

        return 'yokesh nilayam'


home = Home()
print(type(home.home_name) == types.MethodType)  # home_name is the method of class Home


# Generics from typing module
print(list[int] == types.GenericAlias(list, (int,)))
print(dict[str, int] == types.GenericAlias(dict, (str, int)))


print(type(int | str) == types.UnionType) # union type from typing module

print(type(...) == types.EllipsisType) # ... is ellipsis operator





