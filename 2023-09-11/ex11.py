from vin_utils import factorial, line
import sys

def main():
    # print(sys.argv)
    # print(f'user passed {len(sys.argv)} command line arguments to the python command')
    if len(sys.argv) == 1:
        num = input('Enter a number: ')
    else:
        num = sys.argv[1]

    num = int(num)
    f = factorial(num)
    print(f'factorial of {num} is {f}')
    line()
    line('*')
    line('=', 50)
    line(size=50)
    line(char='^')

if __name__ == '__main__': main()

