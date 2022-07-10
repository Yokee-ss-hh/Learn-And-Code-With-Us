# A very simple example of __slot__ attribute.
#
# Problem: Without __slots__
# If I don't have __slot__ attribute in my class, I can add new attributes to my objects.

class Test:
    pass


obj1 = Test()
obj2 = Test()

print(obj1.__dict__)  # --> {}
obj1.x = 12
print(obj1.__dict__)  # --> {'x': 12}
obj1.y = 20
print(obj1.__dict__)  # --> {'x': 12, 'y': 20}

obj2.x = 99
print(obj2.__dict__)  # --> {'x': 99}

# If you look at example above, you can see that obj1 and obj2 have their own x and y attributes and
# python has also created a dict attribute for each object (obj1 and obj2).
#
# Suppose if my class Test has thousands of such objects? Creating an additional attribute dict for
# each object will cause a lot of overhead (memory, computing power etc.) in my code.
#
# Solution: With __slots__
# Now in the following example my class Test contains __slots__ attribute. Now I can't add new attributes to my
# objects (except attribute x) and python doesn't create a dict attribute anymore.
# This eliminates overhead for each object, which can become significant if you have many objects.


class Tests:
    __slots__ = "x"


obj3 = Tests()
obj4 = Tests()
obj3.x = 12
print(obj3.x)  # --> 12
obj4.x = 99
print(obj4.x)  # --> 99

try:
    obj3.y = 28
    print(obj3.y)

except Exception as e:
    print(e)


# An attribute of a class instance has 3 properties: the instance, the name of the attribute,
# and the value of the attribute.
#
# In regular attribute access, the instance acts as a dictionary and the name of the attribute
# acts as the key in that dictionary looking up value.
#
# instance(attribute) --> value
#
# In __slots__ access, the name of the attribute acts as the dictionary and the instance acts
# as the key in the dictionary looking up value.
#
# attribute(instance) --> value
#
# In flyweight pattern, the name of the attribute acts as the dictionary and the value acts as the
# key in that dictionary looking up the instance.
#
# attribute(value) --> instance

