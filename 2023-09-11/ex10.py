from vin_utils import is_prime


def main():
    start = int(input('Enter first number: '))
    end = int(input('Enter second number: '))

    print(f'Here is a list of all prime numbers between {start} and {end}: ')
    for num in range(start, end+1):
        if is_prime(num):
            print(num, end=', ')
    print()
    

if __name__ == '__main__': main()


