#  __post_init__
# This function when made, is called by in-built __init__() after initialization of
# all the attributes of DataClass.
# Basically, object creation of DataClass starts with __init__() (constructor-calling) and
# ends with __post__init__() (post-init processing).

# This feature is very handy at times when certain attributes are dependent
# on the parameters passed in the __init__() but do not get their values directly from them.
# That is, they get their values after performing some operation on a subset of
# arguments received in the constructor.
from dataclasses import dataclass,field

blogs = {'yokesh':'lists','jessy':'tuples','omkar':'dictionaries'}


@dataclass
class Medium:

    author_name : str
    blog : str = field(default = None)

    def __post_init__(self):

        self.blog = blogs[self.author_name]


medium = Medium('yokesh')
print(medium)

# In the above code, We are using __post_init__ to assign 'blog' variable using the author_name that
# was passed by us at the time of object creation. Using this author_name , 'blog' variable got value
# using __post_init__.









