# What is abstraction in python ?

'''
1) An abstract class can be considered as a blueprint for other classes.A class that inherits ABC
   class then it becomes abstract base class.
2) It allows you to create a set of methods that must be created within any
   child classes built from the abstract class.
3) Abstract classes can have abstract methods that are decorated using a abstractmethod decorator
4) Abstract classes can have normal (concrete) methods also.
5) We cannot create an object for an abstract class
6) If any subclass that inherits the abstract class not implements the unimplemented methods in
   abstract class, python raises error
7) Concrete Classes contain only concrete methods while abstract classes contain both concrete
   and abstract methods.
'''
import abc


class Polygon(abc.ABC):     # Abstract Base Class

    def __init__(self,n):

        self.sides = n

    @abc.abstractmethod           # Abstract Method
    def number_of_sides(self):
        pass

    def normal_method(self):      # Concrete Method

        print("Hey I am normal method in abstract base class")


class Rectangle(Polygon):

    def __init__(self,n):

        super().__init__(n)

    def number_of_sides(self):

        print(f"I have {self.sides} sides")


class Triangle(Polygon):

    def __init__(self, n):

        super().__init__(n)

    def number_of_sides(self):

        print(f"I have {self.sides} sides")


class Pentagon(Polygon):

    def __init__(self,n):

        super().__init__(n)


tri = Triangle(3)
tri.number_of_sides()
tri.normal_method()

rect = Rectangle(4)
rect.number_of_sides()
rect.normal_method()

try:
    poly = Polygon(7)   # Error as we cannot create object for the abstract base class

except Exception as e:

    print(e)

try:

    pent = Pentagon(5)

except:

    print("Cannot create as Pentagon class did not implemented abstract method"
          "that was defined in class polygon")

print("*****************************************************************************")

# Do you know that we can implement the same feature of abstraction using subclassing too

# By subclassing directly from the base, we can avoid the need to register the class explicitly.
# In this case, the Python class management is used to recognize PluginImplementation as
# implementing the abstract PluginBase.


class Parent:
    def geeks(self):
        pass


class Child(Parent):
    def geeks(self):
        print("Child class")


# Driver code
print(issubclass(Child, Parent))
print(isinstance(Child(), Parent))

# A side effect of using direct subclassing is, it is possible to find all the implementations
# of your plugin by asking the base class for the list of known classes derived from it.

print("*****************************************************************************")

# In the first example we saw that we can directly use the concrete method which is defined in
# the abstract base class in all of our subclasses using the subclasses objects.

# What if both abstract base class and the immediate subclass has same method name?


class R(abc.ABC):

    def rk(self):
        print("Abstract Base Class R")


class K(R):
    def rk(self):
        print("subclass K")


# Driver code
r = K()
r.rk()

# We will get output as "subclass" as method rk() in class 'K' overrided the method rk() in the
# class 'R'.

# Then, how to call that method in class 'R' ?

# Call from the method rk() which is in subclass 'K' using super()


class R1(abc.ABC):

    def rk1(self):
        print("Abstract Base Class R1")


class K1(R1):
    def rk1(self):
        print("subclass K1")
        super().rk1()


# Driver code
r1 = K1()
r1.rk1()

print("*****************************************************************************")
print("******* Example1 on abstractproperty *********")
# @abstractproperty is deprecated in python 3.3 , so we need to use @property
# on @abstractmethod decorator .
# abstractproperty = @abstractmethod and @property simultaneously on a method.
'''
We may also want to create abstract properties and force our subclass to implement those properties. 
This could be done by using @property decorator along with @abstractmethod.

Since animals often have different diets, we'll need to define a diet in our animal classes. 
Since all the animals are inheriting from Animal, we can define diet to be an abstract property.
Besides diet, we'll make food_eaten property and it's setter will check if we are trying to 
feed the animal something that's not on it's diet.
'''


class Animal(abc.ABC):
    @property
    def food_eaten(self):
        return self._food

    @food_eaten.setter
    def food_eaten(self, food):
        if food in self.diet:
            self._food = food
        else:
            raise ValueError(f"You can't feed this animal with {food}.")

    @property
    @abc.abstractmethod
    def diet(self):
        pass

    @abc.abstractmethod
    def feed(self, time):
        pass


class Lion(Animal):
    @property
    def diet(self):
        return ["antelope", "cheetah", "buffaloe"]

    def feed(self, time):
        print(f"Feeding a lion with {self.food_eaten} meat! At {time}")


class Snake(Animal):
    @property
    def diet(self):
        return ["frog", "rabbit"]

    def feed(self, time):
        print(f"Feeding a snake with {self.food_eaten} meat! At {time}")


leo = Lion()
leo.food_eaten = "antelope"
leo.feed("10:10 AM")
adam = Snake()
adam.food_eaten = "frog"
adam.feed("10:20 AM")

# If we try to feed an animal something that it doesn't eat:
# The setter will raise a ValueError:

try :
    leo1 = Lion()
    leo1.food_eaten = "carrot"
    leo1.feed("10:10 AM")

except Exception as e :

    print(e)


print("******* Example2 on abstractproperty *********")


class Person(abc.ABC):

    @property
    def which_drink(self):

        return self._fav_drink

    @which_drink.setter
    def which_drink(self,name):

        if name in self.favorites:

               self._fav_drink = name
        else:
               raise ValueError("This is not in his favorite drinks, please provide him his favorite drink")

    @property
    @abc.abstractmethod
    def favorites(self):
        pass

    @abc.abstractmethod
    def cost(self,amount):
        pass


class PeopleInTheNorthPole(Person):

    @property
    def favorites(self):

        return ['vodka','whisky','rum']

    def cost(self,amount):

        print(f"He drank {self.which_drink} worth {amount*100} rupees")


protensko_buch = PeopleInTheNorthPole()
protensko_buch.which_drink = 'rum'
protensko_buch.cost(2)


# What if i provide him that is not available in his favorites list ?

try:

    protensko_buch.which_drink = 'coffee'

except Exception as e :

    print(e)


print("*****************************************************************************")
# Final Example on Abstraction


class Employee(abc.ABC):
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    @abc.abstractmethod
    def get_salary(self):
        pass


class FulltimeEmployee(Employee):
    def __init__(self, first_name, last_name, salary):
        super().__init__(first_name, last_name)
        self.salary = salary

    def get_salary(self):
        return self.salary


class HourlyEmployee(Employee):
    def __init__(self, first_name, last_name, worked_hours, rate):
        super().__init__(first_name, last_name)
        self.worked_hours = worked_hours
        self.rate = rate

    def get_salary(self):
        return self.worked_hours * self.rate


class Payroll:
    def __init__(self):
        self.employee_list = []

    def add(self, employee):
        self.employee_list.append(employee)

    def print(self):
        for e in self.employee_list:
            print(f"{e.full_name} \t INR {e.get_salary()}")


payroll = Payroll()

payroll.add(FulltimeEmployee('John', 'Doe', 6000))
payroll.add(FulltimeEmployee('Jane', 'Doe', 6500))
payroll.add(HourlyEmployee('Jenifer', 'Smith', 200, 50))
payroll.add(HourlyEmployee('David', 'Wilson', 150, 100))
payroll.add(HourlyEmployee('Kevin', 'Miller', 100, 150))

payroll.print()

print("*****************************************************************************")

