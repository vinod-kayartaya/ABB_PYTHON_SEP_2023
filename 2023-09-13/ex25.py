from vinutils import Person


def main():
    p1 = Person(name='Vinod')
    p1.print_info()

    p2 = Person(name='Kiran', email='kiran@xmpl.com')
    p2.print_info()

    p3 = Person(name='Ramesh', city='Chennai', state='TN')
    p3.print_info()

    # p1.__email = 'vinod@vinod.co'
    # p1.email('vinod@vinod.co')
    p1.email = 'vinod@vinod.co'  # this is a call to the @setter method email(self, value) in the person class
    print(f'p1.email is {p1.email}')  # this is a call to the @property method email(self) in the Person class

    print(p1)
    print(p2)
    print(p3)
    # the above is same as the below
    print(p3.__str__())  # since dunder attributes are supposed private, we are not expected to call __str__() like this


if __name__ == '__main__':
    main()
