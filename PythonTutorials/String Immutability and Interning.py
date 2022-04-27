'''
1) int, float, strings and tuples are immutable in python
2) Immutable means once the object is created, we cannot change it's content again
3) In simple words, we cannot edit the content what we initialized to that variable
'''

# What is aliasing in python?

'''
'='  operator is used for creating aliasing for existing objects.
Those objects that are involved in aliasing always points to the same memory location
'''

var1 = "python"
var2 = var1     # We did aliasing here

print(id(var1),id(var2)) # Both Id's are same , isn't it ?

# Let's check whether the contents are same too!

print(var1 == var2) # Returns True because both have same content as 'python'

'''
In mutable objects after aliasing , changes made to aliased object will reflect in original object
But, In immutable it won't happen, see the below example to see that
'''

# mutable object,
my_list = [1,2,3]
final_list = my_list
final_list.append(4)
print(final_list)
print(my_list)
print(my_list == final_list) # True
# Look the outputs the both original list and aliased list, both have same content even we changed the content of
# aliased object . This is the mutable property, But the same case we won't observe in strings as strings are immutable.

print("***************************************")
# immutable object,

my_str = "india"
final_str = my_str
print(id(my_str))
print(id(final_str))
print(id(my_str) == id(final_str)) # Returns True
# Until here , we have both original string and aliased string pointing to same memory address
# After we concatenated the aliased string , lets see the id's again below
final_str = final_str+"a"
print(final_str)
print(my_str)
print(id(my_str))
print(id(final_str))
print(id(my_str) == id(final_str)) # Returns False
# Now, The id's of original and aliased strings are not same , because we changed the contents of aliased string
# that is not reflected in original string (my_str)  because of immutable property.

print("***************************************")
# Unchanged strings even after slicing and concatenating always points to the same memory address. Let's prove it !
fav_place = "Munnar"
edited_fav_place = fav_place + ""
print(id(fav_place),id(edited_fav_place))
print(id(fav_place) == id(edited_fav_place))
print(fav_place is edited_fav_place)

fav_dish = "fish"
edited_fav_dish =fav_dish[::]
print(id(fav_dish),id(edited_fav_dish))
print(id(fav_dish) == id(edited_fav_dish))
print(fav_dish is edited_fav_dish)

# Hence Proved :)

print("***************************************")
# What is string Interning ?
# String Interning is a process of storing only one copy of each distinct string value in memory.
'''
String Interning is the process of storing single copy of the string value in the memory.
If there are few string variables storing same value in them, instead of storing all these values at different locations-
-python uses memory optimizer named peephole optimizer(until python 3.7) and AST optimizer (python 3.8+)to store- 
-the object at one place and making all the string variables pointing to this memory location.
This process is called interning and python does it implicitly whenever it finds 2 or more variables of same type have 
same values storing in them.
String Interning saves memory usage by decreasing duplicated values in the memory-
-since storing only one copy needs less space than storing all of them.
In peephole optimizer, strings less than 20 characters are interned.
In AST optimizer, strings less than 4096 characters are interned.
'''
fav_destination = "antarctica"
fav_holiday_spot = "antarctica"
print(id(fav_destination))
print(id(fav_holiday_spot))

print(id(fav_destination) == id(fav_holiday_spot))
print(fav_destination is fav_holiday_spot)

# The Id's of both variables are same because of string interning .

print("***********Some examples on interning**********************")

# Please Remember the lines 235,236 in TextDataType.py file in the same repository, Unchanged strings even after
# applying concatenation and slicing always point to original string memory address only.

a = 'Hello World'
b = 'Hello World'
c = 'Hello Worl'

print(a is b)      # o/p = True
print(a == b)      # o/p = True
print(id(a),id(c+'d'))
print(a is c+'d')  # o/p = False
print(a == c+'d')  # o/p = True

# Why False? Because the '+' operator changing the contents of string 'c' , so new memory is created for c+'d' object.
# Explanation:
'''
1)When string a is created, the compiler checks if Hello World is present in interned memory. 
2)Since it is the first occurrence of this string value, Python creates an object and caches this string in memory 
and points a to this reference.
3)When b is created, Hello World is found by the compiler in the interned memory so instead of creating another string, 
b simply points to the previously allocated memory.
a is b and a == b in this case.
4)Finally, when we create the string c = 'Hello Worl', the compiler instantiates another object in interned memory because 
it could not find the same object for reference.
5)When we compare a and c+'d', the latter is evaluated to Hello World. However, since Python doesn't do interning 
during runtime, a new object is created instead. Thus, since no interning was done, these two aren't the same 
object and is returns False.
6)In contrast to the is operator, the == operator compares the values of the strings after computing runtime expressions 
Hello World == Hello World.
7)At that time, a and c+'d' are the same, value-wise, so this returns True.
'''
print("*********************************************")
# Look at the below example
concat_char = 'e'
name1 = "yokesh"
name2 = "yokesh"
name3 = "yokesh" + 'e'          # executes at compile time
name4 = "yokesh" + concat_char  # executes at runtime

print(id(concat_char))
print(id(name1),id(name2),id(name3),id(name4))
# name1 and name2 are implicitly interned by python interpreter so they have same id's.
# name3 and name4 are formed by concatenation , so they are allocated new memory. name4 is evaluated at runtime-
# - so name4 will have different id.

print("**************************************************")
# Facts about implicit interning
'''
1)Python automatically interns some strings at the moment of their creation. Whether or not a string is interned depends on several factors:
2)All empty strings and strings of length 1 are interned.
3)Up until version 3.7, Python used peephole optimization, and all strings longer than 20 characters were not interned. 
4)However, now it uses the AST optimizer, and (most) strings up to 4096 characters are interned.
5)Names of functions, class, variables, arguments, etc. are implicitly interned.
6)The keys of dictionaries used to hold module, class, or instance attributes are interned.
7)Strings are interned only at compile-time, this means that they will not be interned if their value can't be computed at compile-time.
8)These strings will be interned for example:
a = 'why'
b = 'why' * 5
9)The following expression is computed at runtime thus the string is not interned.
b = "".join(['w','h','y'])
10)Strings having characters apart from ASCII are most likely not going to be interned.
11)If you recall, we said that 'Hello Worl' + letter_d was computed at runtime, and therefore it will not be interned. 
Since there is no consistent standard on string interning, a good rule of thumb to use is the compile-time/runtime idea,
where you can assume that a string will be interned if it can be computed at compile-time.
'''
leader = "Rama"       # compile time execution
fav_leader = "Ram" + 'a'  # compile time execution
most_fav_leader = "".join(['R','a','m','a'])   # Run time execution
leader_letter = 'a'    # compile time execution
fav_king = "Ram"+leader_letter # Run time execution

print(id(leader))
print(id(fav_leader))
print(id(most_fav_leader))
print(id(leader_letter))
print(id(fav_king))

print("**************************************************")
# Explicit Interning
# From the above topics, We know that those string expressions that execute at runtime will always have different id's-
# -when compared to the string expressions that evaluated at compile time.
# But, We can do explicit interning using sys module as,

import sys

burger1 = sys.intern("cheese_burger")
burger_char = 'r'
burger2 = sys.intern("cheese_burge" + burger_char)
# without sys.intern() we will get different id's of both objects. with sys.intern() we will get explicitly interned.
print(id(burger1),id(burger2))

print("***************************************************")
# upto How many characters strings are interned ? We know that upto 4096 characters ! Let's check it

fav_drink = "Cocacola"
popular_drink = "Cocacola"
print(id(fav_drink) == id(popular_drink))

# We get output as True, let's increase number of characters.

fav_movie = "interstellar"*1000
best_movie = "interstellar"*1000
print(id(fav_movie))
print(id(best_movie))
print(id(fav_movie) == id(best_movie))

# Haha, As we see that id's of those 2 variables are different as we exceeded the string value limit of 4096 characters.
# Conclusion :
'''
By using string interning, you ensure that only one object is created even if you define multiple strings with the same content.
'''
# Advantages:
'''
Memory saving , Faster comparisons
'''
# DisAdvantages:
'''
Memory cost to maintain intern table, Time cost to call intern() method
In multi threaded environments : The interned memory (table) is a global resource in a multi-threaded environment whose synchronization needs to be modified. 
                                 This check might only be needed when the interned table is accessed i.e. when a new string is created but it can be expensive.
'''
