from dataclasses import dataclass,asdict,astuple,make_dataclass,field,is_dataclass


@dataclass
class Mango:

    color : str
    season : str
    is_juicy : bool


yellow_mango = Mango('yellow','summer',True)

# Using asdict and astuple we can get the objects data in the respective formats
# asdict() takes the object name as input and returns its associated variable as key and variables value as value.
# astuple() takes the object name as input and returns its variables values in a tuple.

print(asdict(yellow_mango))
print(astuple(yellow_mango))

# We can make a dataclass dynamically at the runtime using make_dataclass method

Beach = make_dataclass('Beach',[('element1',str,),('element2',str),('is_salty',bool,field(default = False))])

my_beach = Beach('sand','water',True)

print(my_beach)

'''
1) First parameter of make_dataclass() should be 'Data Class' Name.
2) Second parameter should be a list of data class variables.
3) Characteristics of each variable should be bounded together using a tuple() separated commas
'''

# We can check whether a class is a dataclass or not

print(is_dataclass(Beach))
print(is_dataclass(Mango))

# We can check whether an object is of type dataclass or not

print(isinstance(yellow_mango,Mango))
print(isinstance(my_beach,Beach))


