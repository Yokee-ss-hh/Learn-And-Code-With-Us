import random
import itertools

print("************************************************************************")
print("*********** Example1 ************")


def generator1(num):

    n = 0
    while n < num:
        yield n
        n+=1


g_obj1 = generator1(5)

# way1
print(list(g_obj1)) # can use iterable like list,tuple,set etc...

#way2
g_obj2 = generator1(5)
for x in g_obj2:
    print(x,end=",")
print('\n')

#way3
g_obj3 = generator1(5)
try:
    print(next(g_obj3))
    print(next(g_obj3))
    print(next(g_obj3))
    print(next(g_obj3))
    print(next(g_obj3))

except :
    print("Out of range")


print("************************************************************************")
print("************** Example 2 ***************")

# send() method.....


def send_example():
    x = 0
    while True:

        x = yield x
        yield x * 10


se = send_example()
print(next(se))
print(se.send(2))
print(next(se))
print(se.send(4))
se.close()

'''
Line 52 : Invokes right-hand expression of line 47, i.e, yield and it returns 0,so line 52 prints 0
After execution of line 52 RHS expression, program pauses there / goes to sleep and control goes to line 53,
and it sends 2 .Now,first yield on line 47 wakes up and that 2 is set to LHS 'x' variable of line 47, after setting 
next yield statement on line 48 is executed and it returns 2*10 = 20.So, 20 is printed.
Now, line 54 invokes line 47 again, that returns RHS i.e, yield x = yield 2 as x = 2 now .So, line 54 prints 2 
Line 55 sets LHS 'x' variable to 4 . Now, 'x' stores 4 .After 'x' is set to 4,line 48 executes and it returns 4*10 = 40.
Line 56 closes the generator object 'se' so that further evaluation is not done on mistake.
'''

# How send() works :
'''
Generator without send() : One way data flow 

==========       yield      ========
Generator |   ------------> | User |
==========                  ========

Generator with send() : two way data flow 

==========       yield       ========
Generator |   ------------>  | User |
==========    <------------  ========
                  send
                
'''
print("************************************************************************")
print("************** Example 3 ***************")


def myfunc():
    x = ""
    while True:
        print("Yielding {} and waiting".format(x))
        x = yield x
        if x is None:
            break
        print("Got {}. Doubling".format(x))
        x = x * 2


g = myfunc()
print(next(g)) # the generator goes to sleep after returning the
# right side but before assigning any value to the left side.

print(g.send(10)) # when it wakes up the first thing that happens is sent value is assigned to
# the left side and yields the value of the x i.e, 20

print(g.send(20))

# send() works same as the next() but it sets the parameter that it has to the left operand , then the -
# - program flow continues.


print("************************************************************************")
print("************** Example 4 ***************")


def pig_latin_sentence(sent):
    output = []
    for word in sent.split():
        if word[0] in "aeiou":
            output.append(word + "ay")
        else:
            output.append(word[1:] + word[0] + "ay")
    return " ".join(output)


def pl_translate():
    sentence = ""
    while True:
        sentence = yield pig_latin_sentence(sentence)
        if sentence is None:
            break


g = pl_translate()
print(next(g))

print(g.send("Python is so awesome right"))

'''
output : 
The execution starts at line 17 and “g” generator object pl_translate is invoked.
Then the execution goes to line 11 and we enter the while loop and the execution comes at line 13 and 
(“right side of the assignment statement is executed”)pig_latin_sentence(sentence) is executed. 
And null string is returned.
Then the execution is halted and we come out of the pl_translate() function and line 20 is executed.
and using the send function we initialize sentence = “Python is so awesome right”,and the execution comes on line 14.
But due to the while loop the execution again comes on line 13 and pig_latin_sentence(sentence) is executed and yielded.
'''

print("************************************************************************")
print("************** Example 5 ***************")


def bad_service_chatbot():
    answers = ["We don't do that",
               "We will get back to you right away",
               "Your call is very important to us",
               "Sorry, my manager is unavailable"]
    yield "Can I help you?"
    s = ""
    while True:
        if s is None:
            break
        s = yield random.choice(answers)


g = bad_service_chatbot()
print(next(g))

print(g.send("ok"))

print(g.send("hello"))


print("************************************************************************")
print("************** Example 6 ***************")


def double_number(number):
     num = number
     while True:
         num = yield num
         yield num-5


c = double_number(4)
for x in range(5):
    print(next(c))
    print(c.send(20))


print("************************************************************************")
print("************** yield from  ***************")

# Speaking at higher level yield from is equivalent to for val in data: yield val


def some_list(sample_list = []):

    for _ in sample_list:
        yield _


for x in some_list([1,2,3,4,5,6,7]):
    print(x,end=",")

print('\n')

y = some_list([2,4,6,8,10])

print(list(y))

print('\n')

z = some_list([1,3,5,7,9])
print(next(z))
print(next(z))
print(next(z))
print(next(z))
print(next(z))

print("************************************************************************")
print("************** Generator Chaining ***************")


def chaining_of_generators(*iterables_group):

    for x in iterables_group:

        for y in x:

            yield y


generator_object = chaining_of_generators((a for a in [2,4,6,8,10]),(b for b in [1,3,5,7,9]))

for item in generator_object:

    print(item,end=',')


print('\n')

# We can do the same thing using itertools.chain() method as,

for items in itertools.chain([2,4,6,8,10],[1,3,5,7,9]):

    print(items,end=',')


print("************************************************************************")
print("************** Generator  throw() method ***************")


def some_thing(x):

    y = 2

    while y < x :
        try :
            yield y
            y+=1
            yield y
            y+=3

        except Exception:
            print("This is raised",Exception.__name__)


s_t = some_thing(20)
print(next(s_t))
print(next(s_t))
s_t.throw(StopIteration)
print(next(s_t))
print(next(s_t))
s_t.throw(FloatingPointError)
print(next(s_t))
print(next(s_t))
s_t.close()

# Using raise() method of generator object, we can raise errors at any point of time.








