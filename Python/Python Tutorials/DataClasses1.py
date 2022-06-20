from dataclasses import dataclass
'''
1) Data classes can be coded using @dataclass decorator
2) While creating Dataclasses we don't have to define a __init__() method as dataclass
   internally defines it after calling with an object.
3) printing the object of a dataclass will call __repr__() magic method internally so that
   developers can understand the properties of the object more precisely.
4) Two data class objects with same data gives 'True' on '==' operator, while Normal concrete classes
   gives 'False'
'''

print("*******************************************************************************************")
print("***** Dataclass vs Concrete class")


@dataclass
class Movie:

    movie_name : str
    cost : float
    place : str
    seat_number : int


movie = Movie('bahubali',432.32,'bangalore',32)
print(movie)
movie1 = Movie('bahubali',432.32,'bangalore',32)
print(movie1)


class Cinema:

    def __init__(self,a : str, b : float, c : str, d : int):

        self.movie_name = a
        self.cost = b
        self.place = c
        self.seat_number = d

    def __repr__(self):

        return f"Cinema(movie_name = '{self.movie_name}', cost = {self.cost}, place = '{self.place}', seat_number = {self.seat_number})"


cinema = Cinema('bahubali',432.32,'bangalore',32)
print(cinema)

cinema1 = Cinema('bahubali',432.32,'bangalore',32)
print(cinema1)
# As you see in dataclasses we don't want to define __init__ manually as we did in concrete
# class and dataclass comes with modified __repr__() method.

# How to know dataclass will define it's __init__() method internally ?

try:
    movie2 = Movie()
    print(movie2)

except Exception as e:

    print(e)

# Exception : Movie.__init__() missing 4 required positional arguments: 'movie_name', 'cost', 'place', and 'seat_number'
# The above exception says that dataclass uses __init__ internally.

# '==' works different on dataclass objects and on concrete classes objects with same data.


print(movie == movie1)

print(cinema == cinema1)


print("*******************************************************************************************")

# Can we override the internal __init__ with our own constructor ?


@dataclass
class GG:

    def __init__(self,a):

        self.item = a


gg = GG(23)
print(gg)
print(gg.item)

# Even though __init__ is overrided __repr__ won't work as __repr__ relies on internal __init__
# and that __init__ enables only when variables are declared in the dataclass


@dataclass(init=False)  # Disables internal __init__
class Vohaaa:
    a: int
    b: int

    def __init__(self, a, b):
        self.a = a
        self.b = b


vohaa = Vohaaa(2, 3)
print(vohaa)

# Now __repr__ worked as we declared variables in the dataclass.
print("*******************************************************************************************")
