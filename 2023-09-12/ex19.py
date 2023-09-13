def main():
    filename = input('Enter a filename to read: ')
    try:
        f = open(filename)
        # content = f.read()
        # print(content)

        # list_of_lines = f.readlines()
        # for line in list_of_lines:
        #     print(line, end='')

        # while True:
        #     line = f.readline()
        #     if line == '': break
        #     print(line, end='')

        for line in f:
            print(line, end='')

        f.close()

    except FileNotFoundError:
        print(f'No file with name "{filename}" was found')


if __name__ == '__main__':
    main()
