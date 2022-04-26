from string import Template


# Strings are immutable objects in Python. This means that once strings are created, we can not change or update them.
# Even if it seems like a string has been modified, under the hood,
# a copy with the modified value was created and assigned to the variable, while the original string remained the same.
# Example:
'''
main_stringg = "Globe sometimes called as Laddu"
main_stringg[3] = 'c'
print(main_stringg)
'''
# Running above 3 lines gives error as strings do not support item assignment.

print("**********************************************************")
# strings in python has a built-in constructor called str()
# strings can be assigned to a variable using single / double quotes
# Un initialized strings are ignored by python interpreter

fname = 'yokesh'
lname = "bollineni"
place = '''He lives in pakala'''
friends_place = """His friends lives in tirupathi, renugunta and Guntur"""

print(type(fname)) # <class 'str'>

# python don't have character arrays , so character is nothing but a string with length 1
my_char = 'A'
print(type(my_char))

print("*********************")
# strings creation using str() constructor
constructed_string = str("This is constructed string")
print(constructed_string)
integer_string = str(1234)
print(integer_string)
floating_string = str(12.2131)
print(floating_string)

print("**********************************************************")
print("*********************string formatting********************")
# method 1 using string formatting operator %
'''
  s for strings
  d for int
  f for float
  c for character
'''
print("Hello my name is %s and lives in %s"%(fname,'pakala'))
print('He is %d years old and earning %f dollars'%(22,2500.2313))

# a.bf
# a would be the minimum number of digits to be present in the string these might be padded with white space if the whole number doesn’t have this many digits. 
# Close to this, bf represents how many digits are to be displayed after the decimal point. 

print("The exact price of oil is %6.3f"%(342.21)) # result is 342.210 , 0 added because 3 is the length we gave for bf
print("Hello world %4.2f"%(2.2341))
print("%5.6f"%(971737817.7937782))
print('The value of pi is: %5.4f' %(3.1))
print("Hello Jhonny%c"%110) # 110 evaluates to p in ascii 
print("*************************************************************")
# method 2 using format() method
print("Hello my name is {} {}".format(fname,lname))
# The above line is same as ,
print("Hello my name is {0} {1}".format(fname,lname))
# changing index values changes string placement as,
print("Hello my name is {1} {0}".format(fname,lname))
# using keyword args,
print("He plays with his dog {dog_name} and with his toy {toy_name}".format(dog_name = "snoopy",toy_name = "Buldo"))
print("The binary to decimal value is : {:d}".format(0b0011))
print("The binary value is : {:b}".format(500))
print("The scientific value is : {:e}".format(40))
print("The scientific value is : {:E}".format(40))
print("The value is : {:f}".format(40))
print("The value is : {:.2f}".format(40))
print("The value is : {:3.3f}".format(4.2342))
print("The value is : {:o}".format(500))
print("The value is : {:x}".format(500))
print("The value is : {:X}".format(500))
print("The value is : {:n}".format(500.00))
print("The value is : {:%}".format(0.80)) # generally takes 6 places in the o/p after decimal point
print("The value is : {:.0%}".format(0.80))
print("The value is {:_}".format(1000000))
print("The value is {:,}".format(1000000))
# The number 5 indicates the space count you want before the number.
print("The value is: {:5}".format(40))
print("The value is: {:+}".format(40))
print("The value is: {:-}".format(-40))
# The number 10 is used to add 10 spaces to show the center-aligned when the value is replaced.\
print("The value {:^10} is positive value".format(40))
# The space of 10 is added using (:>10), and the value replaced is right-aligned.
print("The value {:>10} is positive value".format(40))
# The space of 10 is added using (:<10), and the value replaces is left aligned.
print("The value {:<10} is positive value".format(40))

# using classes with format()
class Wheel:
    tyre = 4
    type = "Normal"
    
print("My car has {obj.tyre} tyres and it is {obj.type}".format(obj = Wheel()))

# dict in format()
my_dict = {'msg1': "Welcome", 'msg2': 'YokiYokee'}
print("{m[msg1]} to {m[msg2]} Villa!".format(m=my_dict))
print("I have {:5} dogs and {:5} cat".format(2,1))

print("******************************************************************")
# method3 using f-strings
my_age = 25
print(f"Call {fname} {lname}")
# In python 3.8 we got new update , we can directly write variable with = operator
# and it will fetch us stored data in that variable.
print(f"His {fname=} and {lname=}")
print(F"Hello {my_age=}")
print(f"His age is {my_age if my_age % 2 == 0 else 23}")
print(f"The square of 8 is {(lambda x : x**2)(8)}")
# we can add precisions as ,
print(f"He has {931.89319737:.2f} dollars")
print(f"The value of 55 in binary is {55:b}")
print(f"The normal value of 1111 is {0b1111:d}")
print(f"I got {0.8:%}")
print(f"He got {0.77:.0%}")
print(f"I got {1000000:,} money")
# padding
print(f"Hello {fname:>10}")  # left padding of 10 white spaces 
print(f"Hello {fname:*>10}") # left padding of 10 white spaces are filled with *
print(f"Hello {fname:^10}")
print(f"Hello {fname:<10}")
# truncating
subject = "Long python tutorials"
print(f"{subject:.10}")
# The precisons what we used for format() method in the above are applicable for f-strings als0.

print("*******************************************************************")
# method 4 using string template class
print(Template("He looks like $some_name").substitute(some_name = "Yokesh"))

bgmi_team = [('yokesh','long shot'),('vineeth','close range'),('sarath','middle men'),('dheeraz','all rounder')]

player = Template("He is $name and his role is $role")
for index in bgmi_team:
    print(player.substitute(name = index[0], role = index[1]))
    
print(Template("My favorite movie is $movie which was released on $Year $month").substitute(movie = "avatar",Year = "2009", month = "august"))

# safe_substitute is used in cases where we don't have matching number of $ and parametres we provide in substitute method.
template = Template('$name is the $job of $company')
string = template.safe_substitute(name='Raju Kumar',job='TCE')
print(string)

# In the above , we have 3 $'s but we gave 2 parametres only , even though we won't get any error because 
# of safe_substitute . For the same example, if we use substitute method we will get error as number of $'s 
# is not matching with the number of parametres given in the substitute method.

#The $$ can be used to escape $ and treat as part of the string. 
print(Template("I want $some_currency $$currency").substitute(some_currency = 1000))
# In the above example ,even we are using substitute but we are not getting error as we used 2 $ symbols
# telling python interpreter to ignore un matched $ .

# Lets print template object
my_template = Template("Hey bro, what's your $age")
print(my_template.template)

temp = Template( 'That $noun looks ${noun}y')
string = temp.substitute(noun='Fish')
print(string)

print("*********************************************************************")
print("********************Escape Characters********************************")
# \'    single quote
# \"    double quote
# \b    backspace
# \ooo  octal value
# \xhh  hexa value
# \r    carriage return
# \n    new line
# \\    backslash
# \f    form feed
# \t    tab space

# Escape Characters are used when we want to insert a character inside a string.
# Basically this string "Hello "world" bro" is a illegal string because , double quotes inside a string 
# isn't allowed.
# Using back slash '\' followed by a character will be ignored by python's interpreter.
print("Hello \"world\" bro") # Need to use \ if we want to insert a double quote inside a double quote
print('Hello "world" bro')   # we dont need a \ if we are inserting double quote inside a single quote
print('It\'s alright')
print("It's alright")
print("I love my \n family") # Creates a new line
print("I love my \t family") # leaves one tab space
print("Hello\bworld") # \b = back space , If we use \b it will erase a previous character inside a string.
# A backslash followed by an 'x' and a hex number represents a hex value:
print("\x48\x65\x6c\x6c\x6f") # \x(some_number), creates a string after converting from hexa decimal to respective character.
# A backslash followed by three integers will result in a octal value:
print("\110\145\154\154\157")
print("cola\\sprite") # backslash is a escape character in python
# \r is called carriage return and it is important escape character in python
# The number of characters after \r is counted and cursor erases that count from the begining and replaces 
# with the characters that are present after \r.
print("python\rgod")
print("Hello\rbe")

print("Hello\
  world\
    beauty")

if(40 > 30 \
  and 90 < 100 \
  and 90 > 40 \
  and 21 > 5):
   print("hi")
# In the above 2 examples we used \ to write single statements in multiple lines , without using \ we will
# get errors if we run those 2 examples.

print("***************************************************************************")
print("****************************Slicing Techniques*****************************")
# Slicing Strings
# slicing creates a new string in the memory , we can do slicing using slice() constructor / [start:stop:step] at the end of the string.
some_quote = "The quick fox jumped over a lazy dog"
print(id(some_quote))
some_quote_sliced = some_quote[0:len(some_quote):1]
print(id(some_quote_sliced))
# In the above line , we did not made any changes to original string (some_quote) using slice operator, so the id's of those 
# 2 strings are pointing to the same memory address.
# Lets concat an empty string to see whether these 2 will point to same address or not .
some_quote_concated = some_quote+""
print(id(some_quote_concated))
# Lets check the memory address are equal using is operator
print(some_quote is some_quote_sliced)
print(some_quote is some_quote_concated)
print(some_quote == some_quote_sliced)
print(some_quote == some_quote_concated)

# We got all outputs as True , that means Unchanged strings even after slicing/concatenating always point to the original string memory address
# and it contains the original string content only .

country1 = "india"
country2 = "dia"
sliced_country1 = country1[2:]
print(id(country1))
print(id(country2))
print(id(sliced_country1))
print(country2 == sliced_country1)
print(country2 is sliced_country1)
# Here sliced output is stored in the memory seperately pointed by sliced_country1, Even though contents of country2 and
# sliced_country1 are equal but their memory locations are different.

print("*************************slicing examples*************************************************")
'''
By default start=index0, stop=last index of string, step=1 (moves from index 0 to last index i.e, from left to right direction)
If we explicitly specify the step as -1 , then start=last index of the string, stop=index 0 of the string.
case1: If start=stop=0 then output is 0
case2: If start<stop and step=-1, then output is 0 , see line 241
case3: If start>stop and step=1, then output is 0 , see line 246,247
case4: If we specify the start=stop=0 then no output, see line 235
'''
print(some_quote[::])
print(some_quote[0:0:]) # By default step = 1, as we wrote stop=0 , iteration starts from start=0 to stop=0 , that means 
# it prints nothing
print(some_quote[0::]) # By default stop=last index of the string and step=1
print(some_quote[2:5])
print(some_quote[3:1:-1])
print(some_quote[::-1])
print(some_quote[::1])
print(some_quote[2:5:-1])
print(some_quote[-1::-1])
print(some_quote[-1::1])
print(some_quote[-2:-4:-1])
print(some_quote[-4::])
print(some_quote[-4:-6:1]) # prints nothing
print(some_quote[-4:-6:]) # By default step=1, so from -4 it moves towards right ,but stop=-6 so it prints nothing.
# We can do slicing using slice() constructor as,
print(some_quote[-4:-2])
print(some_quote[-4:-2:-1])
# slice(start,stop,step)
print(some_quote[slice(0,5,1)])
print(some_quote[slice(-4,-2)])
# print(slice[2:9:1]) gives error as slice() constructor should be inside string/ some other iterable.

print("***********************************************************************")
print("***********************string methods****************************************")
# string methods always return a new string , that means after performing string method operation it always return 
# the new string with new address in the memory.
fav_movie = "i like avatar movie"
fav_series = "Game Of Thrones"

print("*****************************")
# len() : This returns integer i.e, length of a string
print(len(fav_series))
print(len(fav_movie))
print(len(""))
print(len(" "))
print("******************")
# capitalize() : Convert first character to uppercase
capitalized_str = fav_movie.capitalize()
print(capitalized_str)

print("******************")
# title() : converts all first characters of words in a string
print(fav_movie.title())

print("******************")
# upper() : converts all string to uppercase
uppercase_str = fav_movie.upper()
print(uppercase_str)

print("******************")
# casefold() : converts to small case
casefolded_str = fav_series.casefold()
print(casefolded_str)

print("******************")
# lower() : converts to lower case
lowercase_str = fav_series.lower()
print(lowercase_str)

print("******************")
# swapcase() : swaps upper case letters to lower case and viceversa
print(fav_series.swapcase())

print("******************")
# index(character_value,start,stop) : returns the index of the character_value in the string
# By default , start=0 and stop=end of the string
index_value1 = fav_series.index('a')
print(index_value1)
index_value2 = fav_movie.index('a',8,10)
print(index_value2)
# index() gives exception if the character/substring is not found in the range.
# index() method takes start and stop as positive integers only
# print(fav_movie('k',5,2)) gives error as start > stop .
# If the character is not found in the specific range , index() method throws exception . In order to escape from the
# exception we can use find() method.

print("******************")
# find(character,start,stop) : works same as a index() but it won't throws exception and returns -1 when it dont find a character
print(fav_series.find('e',4)) # By default stop = end of the string index
print(fav_series.find('k')) # returns -1 as 'k' is not there in the string

print("******************")
# index() and find() both looks for the first occurence of the character in the given range
# rindex(character,start,stop) and rfind(character,start,stop) both looks for the last occurence of the character in the given range
# By default start=0 and stop=index of the last character in a string
print("yokesh is awesome".rindex('e'))
print(fav_movie.rfind('a'))
# If character not found , rindex() raises exception , where rfind() returns -1

print("******************")
# center() : returns a new string by adding whitespaces by default on the bothsides of the original string.We can specify
# a character in the place of whitespace also.
# center(length_of_the_returned_string,fill_character) by default full_character = whitespace / " "
print("yokesh".center(10))
print("yokiyokee".center(13,"#"))

print("******************")
# count(character,start,stop) : count checks the number of times the character is repeated in the string
print("I love apple, apple are my favorite fruit".count("a"))
print("I love apple, apple are my favorite fruit".count("a",10,20))
print("I love apple, apple are my favorite fruit".count("apple"))

print("******************")
# replace() : This method replaces a word/character in a string with new value , we can specify how many words/characters
# we want to replace.
# replace(old_value,new_value,count) By default count = count of all old values 
print("hello ollaa bella owl ok bro ok bella".replace('ok','gk'))
print("hello ollaa bella owl ok bro ok bella".replace('ok','gk',1)) # replaces first ok occurence only
print("hello ollaa belle owe ok bro ok bella".replace('e','y',4))   # replaces first 4 'e' with 'y'

print("***********************")
# format_map() : Uses dictionary as a parameter
print("HE loves {choco_name} more than {fruit_juice}".format_map({"choco_name":"BlueBerry","fruit_juice":"Fruity"}))
my_dictt = {"abc":123,"xyz":456}
one_str = "He lives in street {abc} near building {xyz}"
print(one_str.format_map(my_dictt))
# Input dictionary
profession = {'name': ['Barry', 'Bruce'],
              'profession': ['Engineer', 'Doctor'],
              'age': [30, 31]}
print('{name[0]} is an {profession[0]} and he'
      ' is {age[0]} years old.'.format_map(profession))

print('{name[1]} is an {profession[1]} and he'
      ' is {age[1]} years old.'.format_map(profession))
print("**************************************")
# removeprefix() and removesuffix()
# You may get a doubt like why we need these 2 methods if we have strip(),lstrip() and rstrip().
# In strip() methods, we need to give a set of characters as parametres that removes those characters from the string
# Using removeprefix() and removesuffix() we can remove a substring directly.
print("Hello world".removeprefix("Hello"))
print("Hello world".removesuffix("world"))

# If the parameter what we give to this methods are not present in the original string, it simply returns the original string.
print("Hello world".removesuffix("Hello"))
print("Hello world".removeprefix("world"))
print("******************")
# For splitting strings , we have 3 methods . They are
# split() , rsplit() and splitlines() , These methods always return a List containing splitted substrings
# split(seperator,limit) : seperator is any white space like \n,\t," " and limit is the integer we specifies.
# IF we specify limit , then we get a list with limit+1 items.
print("Nice laugh by my niece".split()) # takes whitespace as default seperator
print("Nice laugh by my niece".split(' ',3)) 
print("Nice laugh by my niece".split(" ",2))
print("These\ttabs\thave\ttabs\tinside".split('\t'))
print("Thesetabshavetabsinside".split('tabs'))
print("Thesetabshavetabsinside".split('tab'))
print("These\ntabs\nhave\ntabs\ninside".split('\n',8)) # Even we give 8 as limit , list takes 5 items only as \n repeats 4 times only.
print("These\ttabs\thave\ttabs\tinside".split('t'))
print("These\ttabs\thave\ttabs\tinside".split('t',6))  # Even we give 6 as limit , list takes 3 items only as 't' repeats 2 times only.
# The default value of the limit is -1 that means all values .
print("yokesh".split()) # returns list with 1 item i.e, the string itself.
print("my age is aging for agingng while aging".split("ag"))
print("my age is aging for agingng while aging".split("aging"))

print("********************")
# rsplit() works same as split() until the limit is specified.If limit is specified in rsplit() then python
# interpreter starts splitting from right side.
print("Nice laugh by my niece".rsplit())
print("Nice laugh by my niece".rsplit(' ',3)) 
print("Nice laugh by my niece".rsplit(" ",2))
print("These\ttabs\thave\ttabs\tinside".rsplit('\t'))
print("These\ntabs\nhave\ntabs\ninside".rsplit('\n',8))
print("These\ttabs\thave\ttabs\tinside".rsplit('t'))
print("These\ttabs\thave\ttabs\tinside".rsplit('t',6))

print("**********************")
# splitlines() are used to split long string into chunks. The splitting happens at line breaks.
print("Give respect\nTake respect".splitlines())
print("Give respect Take respect".splitlines()) # No splitting happens as there is no line break
splitlines1 = "You\
               Guys\
               Go\
               Ahead\
               I will\
               Look\
               For A\
               Vehicle"
print(splitlines1.splitlines()) # This is not considered as line break as we did it manually using \ operator.
# splitlines() takes one boolean parameter , If True : List item will have \n included , If False : Normal output without \n in list item
print("Give respect\nTake respect".splitlines(True))
print("Give respect\nTake respect".splitlines(False))
# Can use 1 for True and 0 for False
print("Give respect\nTake respect".splitlines(1))
print("Give respect\nTake respect".splitlines(0))

print("**********************************")
# If we specify the character that is not present in the string , it simply returns a list with original string as a element.
print("I love my parents".split('k',3))
print("I love my parents".rsplit("hello"))

print("****************************************")
# partition(some_character/sub_string) : Returns a tuple containing 3 elements 
# the output format : (substring before that specified character,specified character, substring after specified character)
# print("I Love My Parents".partition()) gives error as we did not specified the parameter.
print("I Love My Parents".partition("My"))
# This method searches for the first occurence of the specified character/substring, if our specified character/substring occurs
# at 2 positions , then python takes first occured character/substring.
print("The carzy dog pounced on a sleepy dog with his gang of dogs".partition("dog"))
# If the specified character/substring is not in the string , then also tuple contains 3 elements but the 2nd and 3rd element is empty.
print("How crazy you are".partition("hi"))
print("sofia is sitting on sofa with soffy legs".partition("sof"))

print("************************************")
# rpartition(character/substring) : works same as partition() , but looks for the last occurence of the specified character/substring.
print("I Love My Parents".rpartition("My"))
print("The carzy dog pounced on a sleepy dog with his gang of dogs".rpartition("dog"))
print("How crazy you are".rpartition("hi"))
print("sofia is sitting on sofa with soffy legs".rpartition("sof"))

print("******************************************")
# strip(characters) : Used to remove leading and trailing characters from a given string. By default strip() removes whitespace characters
# We can explicitly provide the characters we want to remove from the given string as well.
print("      Hello        ".strip())
print("A wise man is always wise".strip("A wise")) 
# In the above example First 'A' is removed,then a white space character is removed on both ends,then wise is removed on both leading and trailing
# spaces , then 's' is removed at trailing end as we specified 's' as character in parameter of split().
print("I know you but i wont talk with you".strip("I know you with"))
print(",,,,,rrttgg.....banana....rrr".strip(",rtg."))
print("come on man, its just a man who is coming from comet".strip("comet on man, from"))

print("****************")
# rstrip(characters) : method removes any trailing characters (characters at the end a string), space is the default trailing character to remove.
print("banana,,,,,ssqqqww.....".strip(".wqs,"))
print("Heloooooooooooooooooo      ".strip()) # removes the white space at the right side of the string.
print("Of all movies","interstellar    ".rstrip(),"is my favorite")

print("**********************")
print(",,,,,ssaaww.....banana".lstrip(",saw."))
print("AaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaYeahhhhhhh".lstrip("Aa"))
print("        banana".lstrip())

print("************************************************************")
# ljust(length,some_character) : method will left align the string, using a specified character (space is default) as the fill character.
# length parameter is the length of the returned string after applying ljust() method.
# some_character parameter is the fill value instead of white space.
print("Yokesh".ljust(10))
print("Yokesh".ljust(10,"%"))
# print("Yokesh".ljust()) gives error and says it requires atleast 1 parameter.
# rjust(length,some_character) : method will right align the string,
# using a specified character (space is default) as the fill character.
# some_character parameter is the fill value instead of white space.
print("Various types of mangoes".rjust(30))
print("Various types of mangoes".rjust(30,'&'))
# What if we specify the length in a parameter less than the length of a string? 
# Ans : If just returns the original string only
print("Hello Everyone".rjust(10))
print("Hello Everyone".rjust(10,'^'))

print("***********************************************")
# join() : method takes all items in an iterable and joins them into one string.
# Syntax to use : returned_string = some_character.join(some_iterable)
char_one = " apple "
joined_string = char_one.join(["I love","because i am"]) # joins list elements with apple in between
print(joined_string)

# join() exactly adds some character/substring in between the elements of a iterable
print("e".join(('H','h','h','he')))
print(" ".join(("Hello","World","I love","Music"))) # joins the elements of a tuple with whitespace in between

# If we don't want to give an list/tuple/dict as parameter to join(), we can give a single string as parameter.
print("".join("I am yokesh"))

myDict = {"name": "John", "country": "Norway"}
mySeparator = "TEST"
print(mySeparator.join(myDict)) # By default join() takes keys from dictionary

# We can explicitly specify whether we want to take keys/values as,
print("Test".join(myDict.keys()))
print("Test".join(myDict.values()))

print("*******************************************************")
# zfill(length) : method adds zeros (0) at the beginning of the string, until it reaches the specified length.
# If the value of the len parameter is less than the length of the string, no filling is done.

print("Come on boy".zfill(20))
print("Hello".zfill(3)) # returns "Hello" only as length of the "Hello" < length we specified in zfil()

# print("Hi".zfill()) gives error as we need to give atleast one parameter to zfill().

print("********************************************************")
# expandtabs(tab_size) :  This method sets the tab size to the specified number of whitespaces.
# tab_size is optional parameter and by default tab_size is 8.

print("Y\tO\tK\tE\tS\tH")
print("Y\tO\tK\tE\tS\tH".expandtabs())
# You may think that above line gives error as we did not specified a parameter,
# But that parameter is optional so, expandtabs() takes default parameter i.e, 8 as tab_size.
print("Y\tO\tK\tE\tS\tH".expandtabs(2))
print("Y\tO\tK\tE\tS\tH".expandtabs(4))
print("Y\tO\tK\tE\tS\tH".expandtabs(6))
print("Y\tO\tK\tE\tS\tH".expandtabs(10))

print("*************************************************************")
# maketrans(a,b,c) : These method returns a mapping table that can be used with the
# translate() method to replace specified characters.
'''
1) Parameter 'a':
(Required) If only one parameter is specified, this has to be a dictionary describing how to perform the replace. 
If two or more parameters are specified, this parameter has to be a string specifying the characters you want to replace.
2) Parameter 'b':
(Optional) A string with the same length as parameter x. 
Each character in the first parameter will be replaced with the corresponding character in this string.
3) Parameter 'c':
(optional)  A string describing which characters to remove from the original string.
'''
# Example 1
initial_string = "Lets make a move"
my_table = initial_string.maketrans({'m':'c'})
print(initial_string.translate(my_table))
# Example 2
second_table = initial_string.maketrans("Lam","Gbc")
print(initial_string.translate(second_table))
# Example 3
third_table = initial_string.maketrans("ovs","pwt","Lem")
print(initial_string.translate(third_table))
# Note : lengths of the parameters a and b should be equal to perform example 2.

print("*****************************************************")
print("*************Boolean Returning methods***************")
# endswith(character/substring,start_position,stop_position) :
# Returns True if character is in specified range
# Returns False if character is not in specified range
print("Hello bro welcome to my home".endswith('e'))
print("Hello bro welcome to my home".endswith('e',5,9))
print("Hello bro welcome to my home".endswith('e',7,12))

print("******************")
# startswith(character/substring,start,stop) : Checks whether the string starts with the specified
# character/substring in the given range.
print(fav_movie.startswith('i'))
print(fav_series.startswith('T',8))
print("Hello World".startswith('l',2,7))

print("********")
# isalnum() : checks whether the string is alphanumeric or not
# The string should contain letter (a-z) and numbers (0-9)
print("Hello12387".isalnum())
print("Hello 2387".isalnum())    # o/p is false as white space is there
print("Hello%$12387".isalnum())  # o/p is false as special characters are there
print("********")
# isalpha() : checks whether the string has only alphabets or not
print("GoogleLoveYou".isalpha())
print("Google Love You".isalpha())  # o/p is false as white space is there
print("Google21Love&You".isalpha()) # o/p is false as 21 number and special character & is there
print("************")
# isidentifier() : checks whether the string is identifier or not
# must be (0-9),(a-z) and underscore
# shouldnot start with number / special characters
print("hello_name".isidentifier())
print("23name".isidentifier())
print("my project".isidentifier())
print("*************")
# islower() : Returns True if all characters in a string are lower case
print("world".islower())
print("yokiyokee".islower())
print("India".islower())
print("23mayiooo".islower()) # ignores 23 and starts looking for lowercase from letter 'm'
print("BgMi".islower())
print("***************")
# isupper() : Returns True if all characters in a string are upper case
print("CAKE".isupper())
print("maynoise".isupper())
print("23NETS".isupper()) # ignores 23 and starts looking for uppercase from letter 'N'
print("BgMi".isupper())
print("*****************")
# isprintable() : checks whether the string is printable or not
print("Loving is Good".isprintable())
print("Hating\nis Bad".isprintable())
print("Carry me \r Bro".isprintable())
print("*******************")
# isspace() : Returns True if string has only white space characters
print("".isspace())
print(" ".isspace())
print("He  llo".isspace())
print("*******************")
# istitle() : Checks if all words in a string has the first letter as capital
print("Demo".istitle())
print("Nice Bro !".istitle())
print("He Walked Down There".istitle())
print("99 Ways To WakeUp".istitle())

print("***********There are 3 different headache methods in python strings*******************")
print("************isnumeric() vs isdigit() vs isdecimal()***********************")

# Let's Discuss these 3 methods in detail


print("******************************************************************************")
# Operators with python in detail.
# multiplication operator
print("india"*4)
print('k'*10)
# membership operator
print('m' in "xmas")
print('good' in 'good bye')

