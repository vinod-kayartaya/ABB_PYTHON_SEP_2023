from vinutils import Employee


def main():
    e1 = Employee(id=1234, name='Kishore', city='Mysore', email='kishore@xmpl.com', salary=50000)
    e1.print_info()

    print(f'e1 is {e1}')


if __name__ == '__main__':
    main()
