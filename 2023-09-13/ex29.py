from sqlite3 import connect, DatabaseError


def main():
    # mysql or postgresql configuration
    # config = dict(host='localhost', username='root', password='Welcome#123', database='vindb')
    # for sqlite, it is quite simple. Just the filename
    config = 'vindb.sqlite'

    sql = '''create table customers (
        id INTEGER primary key autoincrement,
        name VARCHAR(50) not null,
        phone VARCHAR(50) unique,
        gender VARCHAR(10) check (gender in ('Male', 'Female')),
        email VARCHAR(150) unique)
    '''

    with connect(config) as conn:
        # conn is like a channel of communication (or like a bridge) between the python app and the db
        cur = conn.cursor()
        # cur represents an object that is capable of executing SQL commands
        try:
            cur.execute(sql)
            print('Table `customers` created')
        except DatabaseError as err:
            print(err)
    # here, conn is closed


if __name__ == '__main__':
    main()
