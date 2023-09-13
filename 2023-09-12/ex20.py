def main():
    filename = input('Enter a filename to read: ')

    try:
        with open(filename) as f:
            for line in f:
                print(line, end='')

    except FileNotFoundError:
        print(f'No file with name "{filename}" was found')


if __name__ == '__main__':
    main()
