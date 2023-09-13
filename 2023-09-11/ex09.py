'''
accept a number and check if it is a prime or not
'''
from vin_utils import is_prime


def main():
    number = int(input('Enter a number: '))
    if is_prime(number): print(f'{number} is a prime number')
    else: print(f'{number} is not a prime number')


if __name__ == '__main__': main()

