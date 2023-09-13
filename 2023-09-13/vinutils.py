class Person:
    def __init__(self, **kwargs):
        if 'name' not in kwargs:
            raise ValueError('`name` is a mandatory property for a Person object')

        self.__name = kwargs.get('name')
        self.__email = kwargs.get('email')
        self.__city = kwargs.get('city', 'Bangalore')

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if type(value) is not str:
            raise TypeError('name must be a string')

        if len(value.strip()) < 3:
            raise ValueError('name muse have at least 3 letters')

        self.__name = value

    @property
    def city(self):
        return self.__city

    @city.setter
    def city(self, value):
        if type(value) is not str:
            raise TypeError('city must be a string')

        self.__city = value

    @property  # this is a readable property for an object of Person class (e.g, p1.email)
    def email(self):
        return self.__email

    @email.setter  # this is a writable property for an object of Person class (e.g, p1.email='vinod@vinod.co')
    def email(self, value):
        if type(value) is not str:
            raise TypeError('email must be a string')

        if len(value.strip()) < 10:
            raise ValueError('email muse have at least 10 letters')

        self.__email = value

    def __str__(self):
        return f'Person(name="{self.__name}", city="{self.__city}", email="{self.__email}")'

    def __eq__(self, other):
        if id(self) == id(other): return True
        if type(other) is not Person: return False

        return self.name == other.name \
            and self.email == other.email \
            and self.city == other.city

    def print_info(self):
        print(f'Name  = {self.__name}')
        print(f'City  = {self.__city}')
        print(f'Email = {self.__email}')


class Employee(Person):
    def __init__(self, **kwargs):

        super().__init__(**kwargs)

        if 'id' not in kwargs:
            raise ValueError('employee id is mandatory')
        _id = kwargs.get('id')
        if type(_id) is not int:
            raise TypeError('employee id must be an int')
        self.__id = _id
        self.__salary = kwargs.get('salary', 25000)

    # over-riding the inherited method
    def print_info(self):
        print(f'ID    = {self.__id}')
        super().print_info()
        print(f'Salary= {self.__salary}')
        print()

    def __str__(self):
        return f'Employee(id={self.__id}, name="{super().name}", email="{super().email}", city="{super().city}", salary={self.__salary})'


def factorial(num):
    if type(num) is not int:
        raise TypeError('only `int` value is expected')

    f = 1
    while num > 1:
        f *= num
        num -= 1
    return f
