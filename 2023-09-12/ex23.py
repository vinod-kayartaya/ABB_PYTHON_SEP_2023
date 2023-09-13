class Person:

    def __init__(self, name, email=None, city='Bangalore', phone=None):
        self.__name = name
        self.__email = email
        self.__city = city
        self.__phone = phone

    def print_info(self):
        print(f'Name     = {self.__name}')
        print(f'Email    = {self.__email}')
        print(f'Phone    = {self.__phone}')
        print(f'City     = {self.__city}')
        print('-'*50)


def main():
    p1 = Person('Vinod', 'vinod@vinod.co', 'Bangalore', '9731424784')
    p2 = Person('James', 'james@xmpl.com', 'Washington', '5023931234')
    p3 = Person('Harish')
    p3.__name = 'Vishal'  # does not change anything!!!

    print(f'type of p1 is {type(p1)}')
    print(f'attributes of p1 are {dir(p1)}')

    p1.print_info()  # p1 is the invoking object, and is passed as the first argument to print_info()
    p2.print_info()
    p3.print_info()


if __name__ == '__main__':
    main()
