def test_fn1():
    print('test_fn1: no parameters for this method')
    print()


def test_fn2(name, email, city='Bangalore'):
    print('test_fn2: this method must be called with exactly 3 arguments')
    print(f'arguments are: name={name}, email={email}, city={city}')
    print()


def test_fn3(*args):
    print('test_fn3: this method can receive any number of arguments')
    print(f'the arguments are received as a tuple. type(args) is {type(args)}')
    print(f'the arguments are: {args}')
    print(f'number of arguments passed are: {len(args)}')
    print()


def avg(*numbers):
    numbers = [n for n in numbers if type(n) in (int, float)]
    return sum(numbers) / len(numbers)


def main():
    test_fn1()
    test_fn2('Vinod', 'vinod@vinod.co', 'Bangalore')
    test_fn2(city='Chennai', name='Ramesh', email='ramesh@xmpl.com')
    test_fn2('Kumar', 'kumar@xmpl.com')
    test_fn2('Rohit', email='rohit@xmpl.com')
    test_fn2(email='mohit@xmpl.com', name='Mohit')
    test_fn3()
    test_fn3('Vinod', 'vinod@vinod.co')
    test_fn3('Vinod', 'vinod@vinod.co', 'Bangalore')
    test_fn3(10, 20, 30)

    average = avg(10, 20, True, False, 'Vinod', 30)
    print(f'average is {average}')


if __name__ == '__main__':
    main()
