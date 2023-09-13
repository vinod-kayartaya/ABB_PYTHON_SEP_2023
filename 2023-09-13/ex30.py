from sqlite3 import connect, DatabaseError


config = 'vindb.sqlite'


def main():
    sql = 'insert into customers (name, email, phone, gender) values (?, ?, ?, ?)'

    with connect(config) as conn:
        cur = conn.cursor()
        while True:
            print('Enter customer details: ')
            name = input('Name  : ')
            email = input('Email : ')
            phone = input('Phone : ')
            gender = input('Gender: ')

            try:
                cur.execute(sql, (name, email, phone, gender))
                print('New record added the `customers` table')
            except DatabaseError as err:
                print(err)

            ans = input('Do you want to add another record? (yes/no): [yes] ')
            if ans == 'no':
                break


if __name__ == '__main__':
    main()
