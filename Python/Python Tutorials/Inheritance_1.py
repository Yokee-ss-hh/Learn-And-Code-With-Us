# Single Inheritance
'''
         A
         |
         |
         B
'''
print('******************  Example1  ********************')


class BaseClass:

    name = 'Yoki'
    _place = 'India'
    __age = 23

    def __init__(self,a,b,c):

        self.a = a
        self._b = b
        self.__c = c

    def __private_method(self):

        print("I am private method of BaseClass")

    def _protected_method(self):

        print("I am protected method of BaseClass")

    def public_method(self):

        print("I am public method of BaseClass")

    @classmethod
    def return_class_variable_using_class(cls):

        return cls.__age

    def return_class_variable_using_object(self):

        return self.__age


class DerivedClass(BaseClass):

    pass


# Parent Class
bc = BaseClass(2,4,6)
print(bc.a)
print(bc._b)
print(bc._BaseClass__c) # Name mangling
print(bc.name)
print(bc._place)
print(bc._BaseClass__age)
# We cannot access private class variable directly, so use one public / protected method that returns
# private variable on calling,
bc.public_method()
bc._protected_method()
# We cannot call private method __private_method outside the class using object.
bc._BaseClass__private_method() # Name mangling


# Child Class
# NOTE : As DerivedClass don't have any content in it,It takes __init__() from the base class
# So, We need to pass the same number of parameters to __init__() like,
# dc = DerivedClass(6,12,18) , This line make use of BaseClass __init__ and initializes
# dc.a = 6, dc.__b = 12 and dc.__c = 18.
# We can do in one more way as, make a __init__() in DerivedClass and Use BaseClass __init__ in it as,
# def __init__(a,b,c): super.__init__()

dc1 = DerivedClass(10,20,30)
print(dc1.a)
print(dc1._b)
print(dc1._BaseClass__c) # As BaseClass is the Parent of this dc1 object
print(dc1.name)
print(dc1._place)
print(dc1._BaseClass__age)

dc1.public_method()
dc1._protected_method()
dc1._BaseClass__private_method()

'''
Final Note : 
1) In the above example, In DerivedClass We don't have __init__() to initialize dc1 object data, still we did that 
because dc1 object takes BaseClass Constructor and make use of it implicitly.
2) All class and instance variables of parent class can be used by child class on inheritance
3) All types of methods in BaseClass can be called by DerivedClass objects 
4) BaseClass objects can get private methods and private instance variables outside the class using name mangling
   technique. But to get private class variable, we need to use public/protected method to return private class variable.
   Syntax : <BaseClass object>._BaseClass__privatevariable
5) DerivedClass objects can get private methods and private instance variables outside the class using name mangling
   technique. Here, In name mangling syntax, we need to use BaseClass not DerivedClass.
   But to get private class variable, we need to use public/protected method to return private class variable.
   Syntax : <DerivedClass object>._BaseClass__privatevariable
6) In name mangling of derived class object, we are using BaseClass name as, We are using __init__ from parent class
   and accessing all instance methods and variables.
7) In the below example, Let's use super() / Base() to import __init__ from Parent to Child
'''
# Accessing class variables using class names and class method
print(BaseClass.name)
print(BaseClass._place)
print(BaseClass.return_class_variable_using_class())
print(DerivedClass.name)
print(DerivedClass._place)
print(DerivedClass.return_class_variable_using_class())

# Accessing class variables using object names and instance method
print(bc.name)
print(bc._place)
print(bc.return_class_variable_using_object())
print(dc1.name)
print(dc1._place)
print(dc1.return_class_variable_using_object())

print('******************  Example2  ********************')


class Milk:

    milk_color = 'White'
    _animal = 'Cow'
    __animal_color = 'Black'

    def __init__(self,p,q,r):

        self.p = p
        self._q = q
        self.__r = r

    def return_private_animal_color(self):

        return self.__animal_color

    def return_private_r(self):

        return self.__r

    @classmethod
    def return_cls_private_vars(cls):

        return cls.__animal_color

class Curd(Milk):

    def __init__(self,p, q, r):

        super().__init__(p, q, r)  # This will be replaced by lines 124,125 and 126


curd = Curd(8,16,24)

print(curd.p)
print(curd._q)
print(curd.return_private_r())
print(curd.milk_color)
print(curd._animal)
print(curd.return_private_animal_color())

milk = Milk(6,12,18)
print(milk.p)
print(milk._q)
print(milk.return_private_r())
print(milk.milk_color)
print(milk._animal)
print(milk.return_private_animal_color())

# Accessing private Class Variables using Class Names

print(Milk.return_cls_private_vars())
print(Curd.return_cls_private_vars())


print('******************  Example3  ********************')

# We saw that we can use the constructor, class variables and instance variables of the base class
# in it's derived classes.
# What if derived class has its own constructor and methods, let's see in action


class Movie:

    type = 'tollywood'
    _area = 'ramoji film city'
    __movie_name = 'Stranger'

    def __init__(self,x,y,z):

        self.x = x
        self._y = y
        self.__z = z

    def public_movie_method(self):

        print("public method of Movie")

    def _protected_movie_method(self):

        print("protected method of Movie")

    def __private_movie_method(self):

        print("private method of Movie")


class Hero(Movie):

    type1 = 'tollywood1'
    _area1 = 'ramoji film city1'
    __movie_name1 = 'Stranger1'

    def __init__(self,height,weight,color):
        self.height = height
        self._weight = weight
        self.__color = color

    def public_hero_method(self):

        print("public method of Hero")

    def _protected_hero_method(self):

        print("protected method of Hero")

    def __private_hero_method(self):

        print("private method of Hero")


movie = Movie(11,22,33)
hero = Hero('6feet','90kg','black-red')

# movie object can access methods,class variables and instance variables of Movie class only /-
print(movie.x)
print(movie._y)
print(movie._Movie__z)
print(movie.type)
print(movie._area)
print(movie._Movie__movie_name)
movie.public_movie_method()
movie._protected_movie_method()
movie._Movie__private_movie_method()

# hero object can access methods,class variables and instance variables of Hero class

print(hero.height)
print(hero._weight)
print(hero._Hero__color)
print(hero.type1)
print(hero._area1)
print(hero._Hero__movie_name1)
hero.public_hero_method()
hero._protected_hero_method()
hero._Hero__private_hero_method()

# hero object can access all class variables of Movie class also,

print(hero.type)
print(hero._area)
print(hero._Movie__movie_name)

# hero object can access all methods of Movie class also,

hero.public_movie_method()
hero._protected_movie_method()
hero._Movie__private_movie_method()


# Can hero object can access instance variables of Movie class movie object??????
# Answer is NO as hero object has no instance variables with names as x,y,z


print('******************  Example4  ********************')
# How to Re-Use parent class constructor and parent class methods in derived class


class AB:

    def __init__(self,a,b):

        self.a = a
        self.b = b

    def parent_class_method(self):

        print("Hello bro how are you",self.__class__)
        print(self.a+self.b)


class CD(AB):

    def __init__(self,a,b):

        AB.__init__(self,a,b)
        # super().__init__(a,b)

    def child_class_method(self):

        # AB.parent_class_method(self)
        super().parent_class_method()


ab_obj = AB(1,2)
ab_obj.parent_class_method()


cd_obj = CD(3,4)
cd_obj.child_class_method()


print("******************* Example5 ********************")


class Yok1:

    def __init__(self,val):

        self.val = val
        print(f"We are in {self.__class__} class")

    def print_val(self):

        print("val variable of Yok1 class object stores :",self.val)


class Yok2(Yok1):

    def __init__(self,val):

        super().__init__(val+10)

    def print_val(self):

        super().print_val()


yok1 = Yok1(10)
yok1.print_val()
yok2 = Yok2(20)
yok2.print_val()


print("******************* Example6 ********************")
# Base and Derived classes having same variable names and same method names


class Water:

    color = 'white'

    def __init__(self,e):

        self.e = e

    def print_data(self):

        print("I am from Water class")


class H2o(Water):

    color = 'black'

    def __init__(self,e):

        self.e = e

    def print_data(self):

        print("I am H2o class")


water_obj = Water(5)
water_obj.print_data()
print(water_obj.e)
print(water_obj.color)
print(Water.color)

h2o_obj = H2o(10)
h2o_obj.print_data()
print(h2o_obj.e)
print(h2o_obj.color)
print(H2o.color)


print("******************* Example7 ********************")


class Train:

    def __init__(self):

        self.boggies = []


class Boggie(Train):

    def __init__(self,grain_bags):

        self.grain_bags = grain_bags


train = Train()
train.boggies.append(Boggie('10 bags'))
train.boggies.append(Boggie('20 bags'))
train.boggies.append(Boggie('30 bags'))
train.boggies.append(Boggie('40 bags'))
train.boggies.append(Boggie('50 bags'))

for obj in train.__dict__['boggies']:

    print(obj.grain_bags,end="->")

print('\n')

# In reverse order,
for obj in reversed(train.__dict__['boggies']):

    print(obj.grain_bags,end='->')

print('\n')
print("**********************************************************************************")

print(isinstance(yok1,Yok1))
print(isinstance(yok2,Yok2))
print(isinstance(yok2,Yok1))
print(issubclass(Yok2,Yok1))
print(isinstance(Boggie('60 bags'),Train))
print("***********************************************************************************")
# Line 429 gives True because Yok2 class inherits Yok1 class




