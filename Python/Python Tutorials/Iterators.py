'''
1) An iterator is an object that contains a countable number of values.
2) An iterator is an object that can be iterated upon, meaning that you can traverse-
 -through all the values.
3) Technically, in Python, an iterator is an object which implements the iterator protocol-
-which consist of the methods __iter__() and __next__() .
4) next() and __next__() should be implemented by the iterator only, if on iterable giver error
5) iter() and __iter__() should be used on iterable only, if on iterator gives another iterator-
 - at the different memory location.

Example for point 4 and 5 :

fruits = ['apple','banana','cherry']

f1_iter = iter(fruits)
print(f1_iter)

f2_iter = iter(f1_iter)
print(f2_iter)
'''

iterable1 = 'yokesh'
iterable2 = [1,2,'a','b',8+8.43j]
iterable3 = ('my_tuple',21,8.987,[21,8.87])
iterable4 = {1,2,3,4,5,'b'}
iterable5 = {'even':20,'odd':13,'prime':7,'negative':-321}
iterable6 = range(5)


print("***** String Iterable *****")

iterator_a1 = iter(iterable1)
print(iterator_a1)
print(type(iterator_a1))  # o/p : <class 'str_iterator'>

iterator_a2 = iterable1.__iter__()
print(iterator_a2)
print(type(iterator_a2))

try:
    print(next(iterator_a1))
    print(iterator_a1.__next__())
    print(next(iterator_a1))
    print(iterator_a1.__next__())
    print(next(iterator_a1))
    print(iterator_a1.__next__())
    print(next(iterator_a1))
# gives exception as next() can't find any value as iterable has no more characters.

except StopIteration:
    print("You have reached end of the string iterable")

# We can use for-loop directly on iter object to get associated values,


for y in iterator_a2:
    print(y,end=",")
print('\n')

print("***** List Iterable *****")

iterator_b1 = iter(iterable2)
print(iterator_b1)
print(type(iterator_b1))  # o/p : <class 'list_iterator'>

iterator_b2 = iterable2.__iter__()
print(iterator_b2)
print(type(iterator_b2))

try:
    print(next(iterator_b1))
    print(iterator_b1.__next__())
    print(next(iterator_b1))
    print(iterator_b1.__next__())
    print(next(iterator_b1))
    print(iterator_b1.__next__())
    print(next(iterator_b1))
# gives exception as next() can't find any value as iterable has no more characters.

except StopIteration:
    print("You have reached end of the list iterable")

for y in iterator_b2:
    print(y,end=",")
print('\n')

print("***** Tuple Iterable *****")

iterator_c1 = iter(iterable3)
print(iterator_c1)
print(type(iterator_c1))  # o/p : <class 'tuple_iterator'>

iterator_c2 = iterable3.__iter__()
print(iterator_c2)
print(type(iterator_c2))

try:
    print(next(iterator_c1))
    print(iterator_c1.__next__())
    print(next(iterator_c1))
    print(iterator_c1.__next__())
    print(next(iterator_c1))
    print(iterator_c1.__next__())
    print(next(iterator_c1))
# gives exception as next() can't find any value as iterable has no more characters.

except StopIteration:
    print("You have reached end of the tuple iterable")

for y in iterator_c2:
    print(y,end=",")
print('\n')

print("***** Set Iterable *****")

iterator_d1 = iter(iterable4)
print(iterator_d1)
print(type(iterator_d1))  # o/p : <class 'set_iterator'>

iterator_d2 = iterable4.__iter__()
print(iterator_d2)
print(type(iterator_d2))

try:
    print(next(iterator_d1))
    print(iterator_d1.__next__())
    print(next(iterator_d1))
    print(iterator_d1.__next__())
    print(next(iterator_d1))
    print(iterator_d1.__next__())
    print(next(iterator_d1))
# gives exception as next() can't find any value as iterable has no more characters.

except StopIteration:
    print("You have reached end of the set iterable")

for y in iterator_d2:
    print(y,end=",")
print('\n')

print("***** Dictionary Iterable *****")

iterator_e1 = iter(iterable5)
print(iterator_e1)
print(type(iterator_e1))  # o/p : <class 'dict_keyiterator'>

iterator_e2 = iterable5.__iter__()
print(iterator_e2)
print(type(iterator_e2))

iterator_e3 = iterable5.__init__()
print(iterator_e3)
print(type(iterator_e3))

# By default it takes keys
try:
    print(next(iterator_e1))
    print(iterator_e1.__next__())
    print(next(iterator_e1))
    print(iterator_e1.__next__())
    print(next(iterator_e1))
    print(iterator_e1.__next__())
    print(next(iterator_e1))
# gives exception as next() can't find any value as iterable has no more characters.

except StopIteration:
    print("You have reached end of the dictionary iterable keys")


# For values we can use,
try:
    print(iterable5[next(iterator_e2)])
    print(iterable5[iterator_e2.__next__()])
    print(iterable5[next(iterator_e2)])
    print(iterable5[iterator_e2.__next__()])
    print(iterable5[next(iterator_e2)])
    print(iterable5[iterator_e2.__next__()])
    print(iterable5[next(iterator_e2)])
# gives exception as next() can't find any value as iterable has no more characters.

except StopIteration:
    print("You have reached end of the dictionary iterable values")

print('\n')
print("***** Range Iterable *****")
iterator_f1 = iter(iterable6)
print(iterator_f1)
print(type(iterator_f1))
iterator_f2 = iterable6.__iter__()
print(iterator_f2)
print(type(iterator_f2))

try:
    print(next(iterator_f1))
    print(iterator_f1.__next__())
    print(next(iterator_f1))
    print(iterator_f1.__next__())
    print(next(iterator_f1))
    print(iterator_f1.__next__())
    print(next(iterator_f1))
# gives exception as next() can't find any value as iterable has no more characters.

except StopIteration:
    print("You have reached end of the range iterable")

for c in iterator_f2:
    print(c,end=",")
print('\n')

print("****************************************************************************")
print("******* How for loop works on iterables *******")
'''
1) Internally, for loop creates iter() object first.
2) Then, it calls next() method every time for iterating through each character.
3) When the last item of the iterable is printed and no more items left in the iterable.
4) for loop comes out of the scope.
'''

for_loop_iterable = ['abc',12,99,4.098]

for element in for_loop_iterable:
    print(element,end=",")
print('\n')
for_loop_iter = for_loop_iterable.__iter__()


while True:
   try:
        print(for_loop_iter.__next__())
        print(for_loop_iter.__next__())
        print(for_loop_iter.__next__())
        print(for_loop_iter.__next__())
        print(for_loop_iter.__next__())

   except StopIteration:

        break

print('\n')
print("***********************************************************************")
print("*********** Custom Iterators ***************")


class PowTwo:
    """Class to implement an iterator
    of powers of two"""

    def __init__(self, max=0):
        self.max = max

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):

     try:
        if self.n <= self.max:
            result = 2 ** self.n
            self.n += 1
            return result
        else:
            raise StopIteration

     except StopIteration:
         print("You reached the limit...")


# create an object
numbers = PowTwo(3)

# create an iterable from the object
i = iter(numbers)

# Using next to get to the next iterator element
for y in range(7):
    print(next(i))


class Even:

    def __init__(self,num):

        self.num = num

    def __iter__(self):

        self.start_pos = 0
        return self

    def __next__(self):

        try :
            if self.start_pos <= self.num:

                temp = self.start_pos
                self.start_pos += 2
                return temp
            else:
                raise StopIteration

        except StopIteration:
            print("Limit Reached")


even = Even(10)

even_iterator = iter(even)

for x in range(7):
    print(next(even_iterator))





class Odd:

    def __init__(self,num):

        self.num = num

    def __iter__(self):

        self.start_pos = 1
        return self

    def __next__(self):

        try :
            if self.start_pos <= self.num:

                temp = self.start_pos
                self.start_pos += 2
                return temp
            else:
                raise StopIteration

        except StopIteration:
            print("Limit Reached")


odd = Odd(10)

odd_iterator = iter(odd)

for x in range(7):
    print(next(odd_iterator))


print("****************************************************************************")
print("******* Infinite Iterators ***********")

print("Lets create a infinite iterator creating multiples of 5 on each next() call,")

class Infinite():

    def __init__(self):

        self.number = 0

    def __iter__(self):

        self.start_pos = 0
        return self

    def __next__(self):

        temp = self.number

        self.number += 5

        return temp


inf = Infinite()
inf_iter = iter(inf)

limit = 100
for x in range(limit):
    print(next(inf_iter))


# If we keep limit as infinite, instead of 100, We keep on getting and printing values until limit has reached!
# Be aware to keep the limit,so that we won't get results until we stop the program manually to stop.
# In custom iterators,
# __init__() is used to set the limit until when we want iterator to iterate
# __iter__() is used to set the starting point where iterator need to start
# __next__() is used to return the first value when next() is called , and to-
# - set the return value when __next__() is called the second time, third time ...so on.
# TO understand the above statements, look at the PowTwo class custom iterator.

print('******************************************************************************')


# 2 iterators on same iterable are different.

my_list = [1,2,3,4,5,6,7,'yokesh']

my_iter1 = iter(my_list)

my_iter2 = iter(my_list)

print(my_iter1,my_iter2)

print(my_iter1 is my_iter2)
print(my_iter1 == my_iter2)


my_string = 'currency'

my_iter3 = iter(my_string)

my_iter4 = iter(my_string)

print(my_iter3,my_iter4)

print(my_iter3 is my_iter4)

print(my_iter3 == my_iter4)

print("*************************************************************************")




