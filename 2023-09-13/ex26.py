from vinutils import Person


def main():
    p1 = Person(name='Kumar')

    print(f'p1 is {p1}')

    p1.name = 'Vinod'
    p1.email = 'vinod@vinod.co'
    p1.city = 'Bengaluru'

    print(f'p1.name is {p1.name}')
    print(f'p1.email is {p1.email}')
    print(f'p1.city is {p1.city}')

    print(f'p1 is {p1}')


if __name__ == '__main__':
    main()
