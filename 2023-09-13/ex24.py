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
    if len(numbers) == 0: return None

    numbers = [n for n in numbers if type(n) in (int, float)]
    return sum(numbers) / len(numbers)


def test_fn4(**kwargs):
    print('test_fn4: this method receives keyword arguments')
    print(f'kwargs = {kwargs}')
    print(f'the type of kwargs is {type(kwargs)}')

    if 'name' in kwargs:
        print(f'hello {kwargs.get("name")}')
    if 'city' in kwargs:
        print(f'what is the weather like in {kwargs["city"]}')

    print()


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

    test_fn4(name='Vinod', city='Bangalore')
    test_fn4(title='Let us C', author='Y Kanitkar', price=299, pages=187)

    d1 = dict(name='Shyam', city='Bangalore', email='shyam@xmpl.com')
    test_fn2(**d1)
    test_fn4(**d1)

    t1 = (10, 20, 30, 40)
    test_fn3(*t1)
    l1 = (12, 34, 56, 78)
    test_fn3(*l1)
    test_fn3(*d1.keys())
    test_fn3(*d1.values())


if __name__ == '__main__':
    main()
