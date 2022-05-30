from functools import reduce
print("****************************************************************************")
print("***** max(),min(),enumerate(),map(),filter(),reduce() and zip() *****")

print("***** max and min on list starts from here *****")
rivers_in_india = ['ganga','yamuna','kaveri','godavari','tapati']
print(max(rivers_in_india))
print(max(rivers_in_india,key = len))
print(min(rivers_in_india))
print(min(rivers_in_india,key = lambda y : y[2:]))

dish_names_india = ['Dal','biryani','Golgappa','curd']
print(max(dish_names_india))
print(max(dish_names_india, key = lambda x : x.upper()))
print(min(dish_names_india))
print(min(dish_names_india,key = lambda z : z[::-1]))


# If we pass empty iterable, we will get error. so we need to provide default parameter.

print(max([],default='yoki'))
print(min([],default='ok'))

even_nums_list = [12,16,8,22,234,1024,9996]
print(max(even_nums_list))
print(max(even_nums_list,key = lambda item : item % 3))

print(min(even_nums_list))
print(min(even_nums_list,key = lambda item : item % 3))


print("***** enumerate() on list starts from here *****")
'''
Often, when dealing with iterators, we also get a need to keep a count of iterations. 
Python eases the programmers’ task by providing a built-in function enumerate() for this task. 
Enumerate() method adds a counter to an iterable and returns it in a form of enumerating object. 
This enumerated object can then be used directly for loops or converted into a list of tuples using the list() method.
enumerate() works same as iter(), enumerate() returns enumerate object, while iter() returns iter object
As enumerate() derives from iter(), we can use __next__() and next() on enumerate object to get items.
'''

# syntax : enumerate(iterable,start_position = 0 by default)

daily_routine = ['eat','code','sleep','repeat']

daily_routine_enumerate1 = enumerate(daily_routine)

print(type(daily_routine_enumerate1))

print(daily_routine_enumerate1) # returns enumerator object

# We can use for loop to access enumerator object elements (or) we can use list() to get list of tuples

print(list(daily_routine_enumerate1))

daily_routine_enumerate2 = enumerate(daily_routine)
for y in daily_routine_enumerate2:
    print(y)

daily_routine_enumerate3 = enumerate(daily_routine)
for x,y in daily_routine_enumerate3:
    print(x,y)

# Without creating enumerate object, we can use enumerate() directly with for loop :
for item in enumerate(daily_routine,start=10):
    print(item)


# As enumerate() implements iterator inside, can enumerate() object has __next__() in it ?
daily_routine_enumerate4 = enumerate(daily_routine)
print(type(daily_routine_enumerate4))
print(daily_routine_enumerate4)
print(daily_routine_enumerate4.__next__())
print(daily_routine_enumerate4.__next__())
print(daily_routine_enumerate4.__next__())
print(daily_routine_enumerate4.__next__())

# Yes, we can use next() method on enumerate object.

# We can use zip(iterable1,iterable2,iterable3............iterable n)

for g in enumerate(zip(['a','e','i','o','u'],[1,2,3,4,5],[9,99,999,9999,99999]),10):
    print(g)

# In the line 73 , zip returns [('a', 1, 9), ('e', 2, 99), ('i', 3, 999), ('o', 4, 9999), ('u', 5, 99999)]

for x,y in enumerate(zip(['a','e','i','o','u'],[1,2,3,4,5],[9,99,999,9999,99999]),200):
    print(x,y)


for x,y in enumerate(zip(['a','e','i','o','u'],[1,2,3,4,5],[9,99,999,9999,99999]),55):
    print(x)
    print(y)


print("***** zip starts from here *****")
# syntax : list(zip(iterable1,iterable2,iterable3,............)) , returns list of tuples
'''
print(zip([a,b,c],[d,e,f],[g,h,i])) = [(a,d,g),(b,e,h),(c,f,i)] 
'''

print(list(zip([1,2,3],[9,10,11],['a','b','c'])))
print(tuple(zip([1,2,3],[9,10,11],['a','b','c'])))
print(set(zip([1,2,3],[9,10,11],['a','b','c'])))
print(dict(list(zip([1,2,3],['a','b','c']))))
# The above line same as,
# dict([(a,'a'),(2,'b'),(3,'c')])

print("********** map function starts from here **************")
# map returns map object which is an iterator
# map() takes 1 function and many iterables as it can,
# The number of iterables should equal to the no: of parameters the function holds.


def add_twenty(a):
    return a+20


map_object1 = map(add_twenty,[1,2,3,4,5])
print(map_object1)
print(type(map_object1))

print(map_object1.__next__())
print(map_object1.__next__())
print(map_object1.__next__())
print(map_object1.__next__())
print(map_object1.__next__())
# Iterating next item gives StopIteration Error

# Can use for-loop
map_object2 = map(add_twenty,[1,2,3,4,5])
print(map_object2)
print(type(map_object2))

for item in map_object2:
    print(item)

# Without map object also, we can directly loop on map() itself,

for x in map(add_twenty,[1,2,3,4,5]):
    print(x,end=",")

print('\n')


# As, map() returns iterator we can directly use list/tuple/set to bind items in the iterator directly
# without using any looping.

print(list(map(add_twenty,[1,2,3,4,5])))
print(tuple(map(add_twenty,[1,2,3,4,5])))
print(set(map(add_twenty,[1,2,3,4,5])))

string_for_map1 = 'yokesh'
print(list(map(list,string_for_map1)))


string_for_map2 = 'python is so good'
print(tuple(map(tuple,string_for_map2)))

# We can use 2 iterables on map also,


def add_2(a,b):
    return a+b


print(list(map(add_2,[1,3,5],[2,4,6])))

# We can use lambda on map() also,
print("********** map with lambda function starts from here **************")

print(list(map(lambda x : x+20,[1,2,3,4,5])))
print(tuple(map(lambda x,y,z : x+y+z,[1,2,3],[4,5,6],[7,8,9])))
print(set(map(lambda y : -y+32,[2,3,5,7,11,13,17,19])))

# map() with different iterables,

print(list(map(lambda x,y,z : x+y-z , [1,2,3],(4,5,6),{7,8,9})))
print(set(map(len,{'one':1,'two':2,'three':3}.keys())))
print(set(map(lambda x : x+2,{'one':1,'two':2,'three':3}.values())))


print("".join(list(map(lambda x : x.upper(),'yokesh'))))

# map on empty iterable returns empty iterable itself.
print(list(map(lambda x : x+x , [])))
print(list(map(lambda x : x+x , ())))
print(list(map(lambda x : x+x , dict())))
print(list(map(lambda x : x+x , {})))

print("********** filter function starts from here **************")

# The filter() method filters the given sequence with the help of a function that tests-
# -each element in the sequence to be true or not.


def check_element(x):

    if x % 2 == 0:
        return True
    return False


print(list(filter(check_element,[1,2,3,4,5])))
print(tuple(filter(check_element,[2,3,5,7,11,13,1,7,19])))


def check_age(age):

    if age < 18:
        return False
    return True


filter_obj1 = filter(check_age,[12,13,18,19,32,77,0,100,-21])
print(filter_obj1)
print(type(filter_obj1))
print(filter_obj1.__next__())
print(filter_obj1.__next__())
print(filter_obj1.__next__())
print(filter_obj1.__next__())
print(filter_obj1.__next__())

filter_obj2 = filter(check_age,[12,13,18,19,32,77,0,100,-21])

for item in filter_obj2:
    print(item,end=",")

print('\n')
# using list,tuple and set

print(list(filter(check_age,[12,13,18,19,32,77,0,100,-21])))
print(tuple(filter(check_age,[12,13,18,19,32,77,0,100,-21])))
print(set(filter(check_age,[12,13,18,19,32,77,0,100,-21])))


# filter using lambda :

# filter +ve integers
print(list(filter(lambda x : x > 0 , [1,-32,0,-7.765,12,100])))

# filter vowels from group a string
print(list(filter(lambda a : True if a in ['a','e','i','o','u'] else False , list("abrakadabradqrohqhmqpijfh"))))


books = [
   {"Title":"Angels and Demons", "Author":"Dan Brown", "Price":500},

   {"Title":"Gone Girl", "Author":"Gillian Flynn", "Price":730},

   {"Title":"The Silent Patient", "Author":"Alex Michaelidis", "Price":945},

   {"Title":"Before I Go To Sleep", "Author":"S.J Watson", "Price":400}
]

print(list(filter(lambda x : True if x['Price'] <= 500 else False,books)))

random_list = [1, 'a', 0, False, True, '0']

print(list(filter(None, random_list)))
# When None is used as the first argument to the filter() function,
# all elements that are truthy values (gives True if converted to boolean) are extracted.

# or we can use bool() directly as,

print(list(filter(bool,random_list)))

# filter on empty iterable returns empty iterable itself.
print(list(filter(lambda x : True if x > 0 else False , [])))
print(list(filter(lambda x : True if x > 0 else False , ())))
print(list(filter(lambda x : True if x > 0 else False , dict().keys())))
print(list(filter(lambda x : True if x > 0 else False , {})))

print("********** reduce function starts from here **************")
# syntax : reduce(function,iterable,default)

'''
1) The reduce() function in python is a part of functools module and doesn't return multiple values, 
it just returns a single value.
2) The function passed as an argument is applied to first two elements of the iterable.
3) After this, the function is applied to the previous generated result and to the next element in the iterable.
4) This process continues until the whole iterable is processed.
5) The single value is returned as a result of applying the reduce function on the iterable.
'''

reduced_item = reduce(lambda x,y : x+y , [1,2,3,4,5,6])
print(reduced_item)
print(type(reduced_item))   # (((((1+2)+3)+4)+5)+6)


def do_product(x,y):
    return x*y


print(reduce(do_product,(2,4,6,8,7,5,3,1))) # (((((((2*4)*6)*8)*7)*5)*3)*1)


print(reduce(lambda x,y : x+y , ['yokesh',' ','loves',' ','python']))


def maxi(a,b):
    return a if a > b else b


def mini(a, b):
   return a if a < b else b


print(reduce(maxi,[3, 5, 2, 4, 7, 1]))
print(reduce(mini,[3, 5, 2, 4, 7, 1]))

print(reduce(lambda a,b : a if a > b else b , [3,5,2,4,7,1]))
print(reduce(lambda a,b : a if a < b else b , [3,5,2,4,7,1]))


# checking all values are True or Not
print(reduce(lambda x,y : bool(x) and bool(y) , [1,0,True,False,{},[]]))
print(reduce(lambda x,y : bool(x) or bool(y) , [1,0,True,False,{},[]]))


# What is the main difference between reduce and for loop, if both does the same job !
# Let's see the difference by calculating sum of items in an iterable.

sum = 0
for item in [2,3,5,7,11,13,17,19]:

    sum += item

print(f"sum with loop = {sum}")

print(f"sum with reduce = {reduce(lambda a,b : a+b ,[2,3,5,7,11,13,17,19])}")

# Both for loop and reduce function produce same correct output and the only difference between the traditional loop-
# -and reduce function is that the latter method outperforms the for loop when the size of the list-
# -is very large as it is very optimized and efficient.

# a 2D list
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# using reduce function for flattening a 2D list
print(reduce(lambda x, y: x + y, matrix))

# using list comprehension for flattening a 2D list
print([i for row in matrix for i in row])


# reduce on empty iterable gives error, but map and filter won't so use 3rd variable in reduce() method
# to avoid that error.

try:
    print(reduce(lambda x,y : x*y ,[]))

except Exception as e :
    print(e)


print(reduce(lambda a,b : a if a % 2 == 0 else b , [], 'yokesh'))
print(reduce(lambda a,b : a if a % 2 == 0 else b , [], 23))
print(reduce(lambda a,b : a if a % 2 == 0 else b , [], [1,2,3,4]))
print(reduce(lambda a,b : a if a % 2 == 0 else b , [], 'this is because of empty iterable to reduce'))

print('\n')

print("********* range iterable **********")

print(list(range(10)))
print(max(range(7)))
print(min(range(8)))


print(range(3))
print(type(range(3)))


print(list(map(lambda x : x+3 , range(0,9,2))))

print(tuple(map(lambda a : a*2 if a % 2 == 0 else a-10 , range(5))))


for item in enumerate(range(5)):
    print(item)

for a,b in enumerate(range(3)):
    print(a,b)


range_enum = enumerate(range(2))
print(next(range_enum))
print(range_enum.__next__())


print(list(zip(range(5),range(6,10))))
print(dict(zip(['a','e','i','o','u'],range(5))))


print(list(filter(lambda a : True if a == 2 else False , range(3))))

print(tuple(filter(lambda y : bool(y) , range(0,1))))

print(reduce(lambda x,y : x+y , range(10)))
print(reduce(lambda a,b : a.upper() + b.lower() , list(chr(item) for item in range(70,75))))














