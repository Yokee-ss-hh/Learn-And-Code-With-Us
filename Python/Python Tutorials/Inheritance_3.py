# Multi-level Inheritance
'''
         A
         |
         |
         B
         |
         |
         C
'''


class Hola:

    def __init__(self,a):
        self.a = a

    def m1(self):

        print('one')
        print('two')


class Hola1(Hola):

    def m1(self):

        print('three')
        super().m1()
        print('four')


class Hola2(Hola1):

    def m1(self):

        print('five')
        super().m1()
        print('six')


h2 = Hola2(10)
print(Hola2.__mro__)
'''
MRO Order :  Hola2 -> Hola1 -> Hola1 -> Object
'''
print(h2.a)
h2.m1()


print("***********************************************************************")


class GFG1:
    def __init__(self):
        print('HEY !!!!!! GfG I am initialised(Class GEG1)')

    def sub_GFG(self, b):
        print('Printing from class GFG1:', b)


# class GFG2 inherits the GFG1
class GFG2(GFG1):
    def __init__(self):
        print('HEY !!!!!! GfG I am initialised(Class GEG2)')
        super().__init__()

    def sub_GFG(self, b):
        print('Printing from class GFG2:', b)
        super().sub_GFG(b + 1)


# class GFG3 inherits the GFG1 ang GFG2 both
class GFG3(GFG2):
    def __init__(self):
        print('HEY !!!!!! GfG I am initialised(Class GEG3)')
        super().__init__()

    def sub_GFG(self, b):
        print('Printing from class GFG3:', b)
        super().sub_GFG(b + 1)


# main function
if __name__ == '__main__':
    # created the object gfg
    gfg = GFG3()

    # calling the function sub_GFG3() from class GHG3
    # which inherits both GFG1 and GFG2 classes
    gfg.sub_GFG(10)

print("******************************************************************************")


class GrandFather:

    def __init__(self,family_name):

        self.family_name = family_name

    def print_grand_father_data(self):

        print("I am from grandfather class")


class Father(GrandFather):

    def __init__(self,x):

        super().__init__(x)

    def print_father_data(self):

        print("I am from father class")
        super().print_grand_father_data()


class Myself(Father):

    def __init__(self,y):

        super().__init__(y)

    def print_my_data(self):

        print("I am from my class")
        super().print_father_data()


yok_obj = Myself('yokesh')
print(yok_obj.family_name)
yok_obj.print_my_data()

print("******************************************************************************")
print(issubclass(Myself,Father))
print(issubclass(Myself,GrandFather))
print(issubclass(Father,GrandFather))

print(isinstance(yok_obj,Myself))
print(isinstance(yok_obj,Father))
print(isinstance(yok_obj,GrandFather))


