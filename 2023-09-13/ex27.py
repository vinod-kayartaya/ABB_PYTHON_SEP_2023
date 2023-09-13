from vinutils import Person


def main():
    p1 = Person(name='Vinod', email='vinod@vinod.co')
    p2 = Person(name='Vinod', email='vinod@vinod.co')
    p3 = Person(name='Vinod', email='vinod@gmail.com')
    p1a = p1

    print(f'p1 is {p1} and id(p1) is {id(p1)}')
    print(f'p1a is {p1a} and id(p1a) is {id(p1a)}')
    print(f'p2 is {p2} and id(p2) is {id(p2)}')
    print(f'p3 is {p3} and id(p3) is {id(p3)}')

    print(f'p1==p2 is {p1 == p2}')  # same as p1.__eq__(p2)
    print(f'p1==p1a is {p1 == p1a}')
    print(f'p1==p3 is {p1 == p3}')
    print(f'p3==p2 is {p3 == p2}')


if __name__ == '__main__':
    main()
