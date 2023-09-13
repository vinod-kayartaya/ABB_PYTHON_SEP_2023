def main():
    names = ['Vinod', 'Shyam', 'Harish', 'Ramesh', 'Arun']
    print(names)

    names.append('Rohit')
    names.insert(0, 'Anil')

    print(names)
    name_to_delete = input('Enter a name to delete from the list: ')

    if name_to_delete in names:
        names.remove(name_to_delete)
    else:
        print(f'"{name_to_delete}" was not found in the list')

    for name in names:
        print(name)


if __name__ == '__main__':
    main()
