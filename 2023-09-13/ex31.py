from sqlite3 import connect, DatabaseError


config = 'vindb.sqlite'


def main():
    sql = 'select * from customers where id = ?'

    with connect(config) as conn:
        cur = conn.cursor()
        customer_id = int(input('Enter customer id to search: '))

        cur.execute(sql, (customer_id, ))
        data = cur.fetchone()

        if data is None:
            print(f'No customer record found for id {customer_id}')
        else:
            print(f'Name   : {data[1]}')
            print(f'Gender : {data[3]}')
            print(f'Email  : {data[4]}')
            print(f'Phone  : {data[2]}')


if __name__ == '__main__':
    main()
