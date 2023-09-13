import sys


def main():
    try:
        num = sys.argv[1]
        den = sys.argv[2]

        num = int(num)
        den = int(den)

        quot = num // den

        print(f'{num} // {den} = {quot}')
    except IndexError:
        print('Not enough values supplied')
    except ValueError:
        print('Only integer values are expected')
    except ZeroDivisionError:
        print('Cannot divide a number by zero')

    print('End of main()')


if __name__ == '__main__':
    main()
