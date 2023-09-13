# print(f'ex07 is under execution and the value of __name__ is {__name__}')

from ex06 import give_max

def main():
    n1 = int(input('Enter number 1: '))
    n2 = int(input('Enter number 2: '))

    big = give_max(n1, n2)
    print(f'max between {n1} and {n2} is {big}')


if __name__ == '__main__':
    main()