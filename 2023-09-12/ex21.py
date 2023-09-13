def print_book_details(b):
    if type(b) != dict:
        raise ValueError(f'Expected a dict, but got a {type(b)}')

    for i in b.items():
        print(f'{i[0]} => {i[1]}')


def main():
    book = {'title': 'let us c', 'price': 299}

    while True:
        key = input('Enter key: ')
        if key == '': break

        if key in book:
            print(f'this key already exists with a value of "{book[key]}"')
            continue

        value = input('Enter value: ')
        book[key] = value

    print_book_details(book)
    # print(book)


if __name__ == '__main__':
    main()
