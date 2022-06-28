# Hierarchical Inheritance
'''
          A
          |
          |
     -------------
     |           |
     |           |
     B           C
'''


# Python code to demonstrate example of
# hierarchical inheritance

class Details:

    def __init__(self,id,name,gender):
        self.__id = id
        self.__name = name
        self.__gender = gender

    def show_data(self):
        print("Id: ", self.__id)
        print("Name: ", self.__name)
        print("Gender: ", self.__gender)


class Employee(Details):  # Inheritance

    def __init__(self,id,name,gender,company,dept):
        super().__init__(id,name,gender)
        self.__company = company
        self.__dept = dept

    def show_employee(self):
        super().show_data()
        print("Company: ", self.__company)
        print("Department: ", self.__dept)


class Doctor(Details):  # Inheritance

    def __init__(self,id,name,gender,hospital,dept):
        super().__init__(id, name, gender)
        self.__hospital = hospital
        self.__dept = dept

    def show_employee(self):
        super().show_data()
        print("Hospital: ", self.__hospital)
        print("Department: ", self.__dept)


print("Employee Object")
employee = Employee(123,'yokesh','male','google','back-end')
employee.show_employee()
print('\n')
print("Doctor Object")
doctor = Doctor(32467,'yoki','male','yok_care','surgery')
doctor.show_employee()
print('\n')
# Employee and Doctor classes can access show_data() method in Details class too,
employee.show_data()
print('\n')
doctor.show_data()

print("*******************************************************************************")
print(isinstance(employee,Employee))
print(isinstance(doctor,Doctor))
print(issubclass(Doctor,Details))
print(issubclass(Employee,Details))
print(isinstance(doctor,Details))
print(isinstance(employee,Details))
