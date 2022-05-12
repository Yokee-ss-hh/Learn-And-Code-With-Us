'''
There are 3 sequence data types in python
1) list
2) tuple
3) range
'''
import string
print("***********************************************LISTS************************************************")
'''
1) Uses [] square brackets
2) These are mutable data types
3) Can use Slicing here
4) Can be used as array data structure
5) It can store int, float, complex, list, tuple, dict, set, frozenset, etc as elements
'''
# List has 4 properties.
# Mutable, Indexed , Ordered , Allows duplicates and Changeable.
print("****list()****")
a = {'a':1,'b':2,'c':3}
b = (1,2,3,'hello')
print(f'List from tuple : {list(b)}')
print(f'List from Dictionary : {list(a)}')
print(f'List from Dictionary keys : {list(a.keys())}')
print(f'List from Dictionary values : {list(a.values())}')
print("****************************************************************")
l1 = [1,2.43,3+9j,"hi"]
print(type(l1))
print(id(l1))

# Let's change the order of the elements

l2 = [3+9j,"hi",2.43,1]
print(type(l2))
print(id(l2))

print(l1 == l2)  # False because order of elements in both lists are not matching.
print(l1 is l2)

print(l1[2] == l2[0])       # Due to Interning
print(id(l1[2]),id(l2[0]))  # Due to Interning

# Let's discuss more about memory techniques at the end of the file.
print("*******************************************************")
print("Lists allow duplicates")
duplicate_list = [1,2,2,"yoki","yoki"]
print("List with duplicates : ",duplicate_list)

print("*******************************************************")
print("Length of the list using len()")
print(len(l1))
print(len(l2))

print("*******************************************************")
print("Using list() constructor")
# list() constructor literally converts any sequence into list when given as a parameter.
list_constructor1 = list((1,2,3))
print(list_constructor1)
list_constructor2 = list([1,2,3,4,5,6])
print(list_constructor2)
list_constructor3 = list({99,999,9999})
print(list_constructor3)
print(type(list_constructor1))
print(type(list_constructor2))
print(type(list_constructor3))
# Should give inner brackets [],() or {} to bind all elements together.

# strings are splitted to individual elements while passed to a list() constructor.
print(list('yokesh'))
print(list(" "))


print("*******************************************************")
print("List Slicing using slice [start:stop:step]")
list_slice = ['apple','banana',123,999,3+9.9j,True,2.222,'yokesh']
print(list_slice[3])
print(list_slice[-3])
print(list_slice[1::1])
print(list_slice[::])
print(list_slice[2:5])
print(list_slice[:4])
print(list_slice[::-1])
print(list_slice[1:6:-1]) # Returns Empty List
print(list_slice[-3:-6:1]) # Returns Empty List
print(list_slice[1:6:1])
print(list_slice[-3:-6:-1])
print(list_slice[::2])
print(list_slice[::-2])


print("***********************************************************")
print("Changing Elements in a list using slicing and insert() method")

print("**fav movies example**")
fav_movies = ["avatar","Khaleja","bahubali","RRR"]
fav_movies[1:4] = ["Interstellar","Darling","Orange"]
print(fav_movies)
print(len(fav_movies))

print("**fav fruits example**")
# Case1:
# If we initialize more elements in a list than we specified, the list will dynamically increases.
fav_fruits = ['mango','apple','banana','cherry','blue berry']
fav_fruits[1:3] = ['grape','orange','kiwi']
# can use ('grape','orange','kiwi') also, will get same output
# can use {'grape':1,'orange':2,'kiwi':3} also, will get same output
# can use {'grape':1,'orange':2,'kiwi':3}.keys() also , will get same output.
# If we use {'grape':1,'orange':2,'kiwi':3}.items() then o/p will be,
# output : ['mango', ('grape', 1), ('orange', 2), ('kiwi', 3), 'cherry', 'blue berry']
print(fav_fruits)
print(len(fav_fruits))

print("**fav places example**")
# Case2:
# If we initialize less elements in a list than we specified, the list will dynamically decreases.
fav_places = ['kasaragod','tirupati','thanjavur','goa']
fav_places[1:3] = ['india']
print(fav_places)
print(len(fav_places))

print("**favv fruits example**")
# If we assign normal string without [] brackets then the list will increase in both the cases.
favv_fruits = ['mango','apple','banana','cherry','blue berry']
favv_fruits[1:3] = 'rose apple'
print(favv_fruits)
print(len(favv_fruits))

print("**favv places example**")
favv_places = ['kasaragod','tiruopati','thanjavur','goa']
favv_places[1:3] = 'india'
print(favv_places)
print(len(favv_places))

print("**fav_foods example**")
# we can change the element in the existing list using insert() method as ,
fav_foods = ["Biryani","Mutton","Burger"]
print(fav_foods)
fav_foods.insert(3,"fruits")
print(fav_foods)
fav_foods.insert(1,"salad")
print(fav_foods)

print("**qualities example**")
# What if length of the list is 3 and we give the index as 4 and insert an element,
qualities = ['be patient','cool','reduce anger',]
qualities.insert(4,'go to gym')
print(qualities)

# In the above snippet, qualities list has 3 elements with length of 3 with last element index of 2.
# I tried to insert at index 4 that is not there in the list, still element inserted at the last,
# of the list at index 3. That means if we specify the index greater than the last index of the list,
# the element will insert at the immediate next index of last index of the list.

# Can we insert a list in insert() method,
qualities.insert(0,[1,2,3])
print(qualities)


print("**even numbers example**")
even_numbers = [2,4]
even_numbers.insert(2,[6,8,10])
print(even_numbers)
even_numbers.insert(3,(12,14,16))
print(even_numbers)
even_numbers.insert(4,{'sixteen':16,'seventeen':17}.keys())
print(even_numbers)
even_numbers.insert(5,{'eighteen':18,'nineteen':19}.values())
print(even_numbers)
even_numbers.insert(6,{'twenty':20,'twenty one':21}.items())
print(even_numbers)
even_numbers.insert(7,{'one':1,"two":2})
print(even_numbers)

print("******************************************************")
print("changing elements in a list using extend() and append() methods")
# append() method always adds an element at the end of the list.
print("**append() examples**")
oceans =['indian','pacific']
print("original oceans list is :",oceans)
oceans.append('atlantic')
print("oceans list after appending single element atlantic is :",oceans)
oceans.append(['arctic','arabic'])
print("oceans list after adding some ocean names",oceans)
seas = []
seas.append(['bay of bengal'])
print(seas)
# TO add one list to another use extend() method
print("**extend() examples**")
name1 = ['yokesh','B']
name2 = ['googler','google']
name1.extend(name2)
print(name1)
his_name = []
his_name.extend(['yokesh'])
print(his_name)
# Adding 2 lists to form another list using + operator
my_hobbies = ['studying','gaming']
my_another_hobbies = ['listening music']
my_final_hobbies = my_hobbies + my_another_hobbies
print("Final Hobbies",my_final_hobbies)

print("************************************************************************")
print("Removing elements from a list examples")
laptops = ['dell','hp','apple','windows','lenovo']
# remove takes an element as a parameter and removes that element.
laptops.remove(laptops[2])
print('After Removing apple laptop from laptops :',laptops)
laptops.remove('hp')
print('After Removing hp laptop from laptops :',laptops)

# pop takes index of the list and removes element at that index.
# If no index is given, then it removes the last item in the list.
games = ['bgmi','pubg','call of duty','free fire','asphalt']
games.pop(2)
print(games)
games.pop()
print(games)

# clear empties the list and the reference is there in the memory.
clear_list = [1,2,3,'a','b','c']
clear_list.clear()
print(clear_list,id(clear_list))

# del deletes the entire list from the memeory.
countries = ['india','bhutan','nepal']
del countries
# print(id(countries))
# Printing countries will give us Name Error as , NameError: name 'countries' is not defined

print("************************************************************************")
print("**List Comprehension**")

print([x if ord(x) > 110 else 'less than 110' for x in ['y','o','k','e','s','h']])
print([item for item in ['abc','XYZ','Wrong','Its Ok'] if item.islower()])
print([x+y for x in [1,2,3] for y in [10,20,30]])

def check_valid_username(some_name : str):
    for x  in some_name:
        if x.isdigit() or x in string.punctuation :
            return False
    return True
print([user_name if check_valid_username(user_name) else 'Invalid Name' for user_name in ['yokesh','albert123','francis$#']])

print([x**2 for x in range(1,5)])

print([x[::-1] for x in ['yokesh','sanskrit']])

# display only odd numbers from a list
print([x if x & 1 else 'This Number is even, so cannot display' for x in [123,456,789,222]])

# display only even numbers from a list
print([x if not(x & 1) else 'This Number is odd, so cannot display' for x in [123,456,789,222]])

# forming 2-d matrix,
print([[x,x+1,x+2,x+3] for x in range(0,4)])

# Let's Transpose
my_twoD_matrix = [[1,2,3],
                  [4,5,6],
                  [7,8,9]]

print([[j[i] for j in my_twoD_matrix] for i in range(len(my_twoD_matrix))])

print("*************************************************************************")
print("**sorting lists**")
num_list = [9,33,21,4,1]
num_list.sort()   # By default sort() makes ascending sorting.
print(num_list)

even_list = [20,14,6,8,18,12]
even_list.sort(reverse = True)
print(even_list)

# We can use reverse() function directly
normal_list = ['a','b','c']
normal_list.reverse()
print(normal_list)

# sorted() takes an iterable and sorts that iterable and returns it.
prime_list = [2,3,5,7,9,11,13]
sorted_prime_list = sorted(prime_list)
print(sorted_prime_list)

string_list = ['zebra','apple','aloevera','copenhagen','boat','boar']
string_list.sort()
print(string_list)

# If we have a list with both upper and lower case elements, upper case are sorted first, then lower case.
milk_types = ['White milk','lite white milk','Dark milk','yellow milk','Brown milk']
milk_types.sort()
print(milk_types)
# Use reverse = True to sort in reverse order.


# Custom Sorting using key = function parameter.
my_top_companies = ['google','Apple','tesla','Coin base','Microsoft','meta']
my_top_companies.sort(key = lambda x : x.lower())
print(my_top_companies)


my_best_companies = ['Google','apple','Clarivate','coinbase']


def some_random_func(element):
    return element.upper()


my_best_companies.sort(key = some_random_func)
print(my_best_companies)

favv1 = sorted(my_top_companies, key = lambda x : x[3])
print(favv1)


favv2 = sorted(my_best_companies, key = lambda y : y[::-1])
print(favv2)

random_numbers = [17,78,91,62]
random_numbers.sort(key = lambda x : x % 2)
print(random_numbers)

print("**NOTE**")
print("********")
'''
As list is a mutable data type, almost all the list methods won't create a new list in the memory.
some methods return new lists such as sorted(), copy(), deepcopy(), Concatenation '+',count() , index().
'''

print("**************************************************************************")
print("**copying lists**")
import copy

liss1 = [1,"one",2,"two"]
print(liss1)

liss2 = liss1   # copying via aliasing
print(liss2)

liss3 = liss1.copy()
print(liss3)

liss4 = copy.deepcopy(liss1)
print(liss4)

liss5 = copy.copy(liss1)
print(liss5)
# Will explain how memory is utilized and managed for lists soon,

print("*************************************************************************")
print("**count and index**")
var1 = [1,2,2,2,33,99,9,8,7,9,7,3,4].count(7)
var2 = [1,2,2,2,33,99,9,8,7,9,7,3,4].count(2)
print(var1,var2)

var3 = ['apple','banana','jack','cherry','apple'].count("apple")
print(var3)

# iterable.index(element,start,stop)
var4 = [1,2,2,2,33,99,9,8,7,9,7,3,4].index(2)
var5 = [1,2,2,2,33,99,9,8,7,9,7,3,4].index(2,2,5)
var6 = [1,2,2,2,33,99,9,8,7,9,7,3,4].index(9,9,12)
print(var4,var5,var6)


print("**Builtin methods on list**")
print(max([1,2,3,4,5,6,7]))
print(min([0,12,32,21,9,3]))
print(sum([1,3,5,7,9,2,4,6,8,10]))
# sum(iterable,start): adds up all the elements in an iterable and finally adds start parameter to it.
print("sum is :",sum([1,2,3,4,5],5))
# reversed basically returns an iterator that is used to iterate through list to get elements in reverse order.
print("****")
some_iter = reversed([99,21,321,10,55,79])
for item in some_iter:
    print(item,end = "\n")

print("**********************************************************************************")
print("**Looping**")
# Looping through lists
for some_item in range(len(my_hobbies)):
    print(my_hobbies[some_item],end=" ")

print("\n")
for y in my_best_companies:
    print(y,end = " ")

print("**********************************************************************************")
print("**Concatenation and Repetetion**")
r1 = [1,2,3]
r2 = [4,5,6]
print(r1+r2)

print(r1*2)
print(r2*4)

print("*********************************************************************************")
