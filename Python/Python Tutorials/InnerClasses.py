'''
A class defined in another class is known as an inner class or nested class.
If an object is created using child class means inner class then the object can also
be used by parent class or root class.
A parent class can have one or more inner classes but generally inner classes are avoided.
We can make our code even more object-oriented by using an inner class.
A single object of the class can hold multiple sub-objects. We can use multiple sub-objects to
give a good structure to our program.
'''
print("********************************************************************************")


class Tea:

    def __init__(self,ingredient1,ingredient2,ingredient3):

        self.milk_quantity = ingredient1
        self.tea_powder_quantity = ingredient2
        self.sugar = self.Sugar(ingredient3)

    def tea_contains(self):

        return f"Tea Contains {self.milk_quantity}, {self.tea_powder_quantity} and {self.sugar.sugar_method()}"

    class Sugar:

        def __init__(self,ingredient3):

            self.sugar_quantity = ingredient3

        def sugar_method(self):

            return self.sugar_quantity


tea = Tea("2 small cups","2 full spoons","3 full spoons")

print(tea.tea_contains())

# We can call sugar_method in 2 ways,

print(tea.sugar.sugar_quantity)
print(tea.sugar.sugar_method())

print("********************************************************************************")


class Color:

    # constructor method
    def __init__(self):

        # object attributes
        self.name = 'Green'
        self.lg = self.Lightgreen()

    def show(self):

        print("Name:", self.name)

    # create Lightgreen class
    class Lightgreen:

        def __init__(self):
            self.name = 'Light Green'
            self.code = '024avc'

        def display(self):

            print("Name:", self.name)
            print("Code:", self.code)


# create Color class object
outer = Color()

# method calling
outer.show()

# create a Lightgreen
# inner class object
g = outer.lg

# inner class method calling
g.display()

'''
Why Inner Classes ? 

For the grouping of two or more classes. 
Suppose we have two classes remote and battery. 
Every remote needs a battery but a battery without a remote won’t be used. 
So, we make the Battery an inner class to the Remote. It helps us to save code. 
With the help of the inner class or nested class, we can hide the inner class from the outside world. 
Hence, Hiding the code is another good feature of the inner class. 
By using the inner class, we can easily understand the classes because the classes are closely related.
We do not need to search for classes in the whole code, they all are almost together.
Though inner or nested classes are not used widely in Python it will be a better feature 
to implement code because it is straightforward to organize when we use inner class or nested class.
'''

# Multiple Inner classes means 2 or more classes inside a single class
# Multilevel Inner classes means inner classes inside a inner class and so on........

# Multiple:
print("********************************************************************************")


class Doctor:

    def __init__(self,hosp_name,doc_name1,yoe1,doc_name2,yoe2):

        self.hospital_name = hosp_name
        self.cardiac_doctor = self.Cardiac(doc_name1,yoe1)
        self.neuro_doctor = self.Neuro(doc_name2,yoe2)

    def print_hospital(self):

        print(self.hospital_name)

    class Cardiac:

        def __init__(self,doc_name1,yoe1):

            self.cardiac_doctor_name = doc_name1
            self.cardiac_doctor_name_yoe = yoe1

        def about_cardiac(self):

            print(f"{self.cardiac_doctor_name} has about {self.cardiac_doctor_name_yoe} years experience")

    class Neuro:

        def __init__(self, doc_name2, yoe2):
            self.neuro_doctor_name = doc_name2
            self.neuro_doctor_name_yoe = yoe2

        def about_neuro(self):
            print(f"{self.neuro_doctor_name} has about {self.neuro_doctor_name_yoe} years experience")


doctor = Doctor('KuYo','kus',10,'yok',8)
doctor.print_hospital()

cardiac_object = doctor.cardiac_doctor
cardiac_object.about_cardiac()

neuro_object = doctor.neuro_doctor
neuro_object.about_neuro()

# Multilevel:
print("********************************************************************************")


class Outer:

    def __init__(self):

        self.inner = self.Inner()
        self.innerinner = self.inner.InnerInner()

    def show_classes(self):

        print("This is Outer class")
        print(self.inner)

    class Inner:

        def __init__(self):

            self.innerinner = self.InnerInner()

        def show_classes(self):

            print("This is Inner class")
            print(self.innerinner)

        class InnerInner:

            def inner_display(self, msg):

                print("This is multilevel InnerInner class")
                print(msg)

        def inner_display(self, msg):

            print("This is Inner class")
            print(msg)


outer_obj = Outer()

inner_obj = outer_obj.inner
# OR inner_obj = outer_obj.Inner()

innerinner_obj = inner_obj.innerinner
# OR innerinner_obj = outer_obj.Inner().InnerInner()

innerinner_obj.inner_display('Hello from yokesh')

print("********************************************************************************")








