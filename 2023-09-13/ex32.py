from sqlite3 import connect, DatabaseError


config = 'vindb.sqlite'


def main():
    sql = 'select * from customers'

    with connect(config) as conn:
        cur = conn.cursor()

        cur.execute(sql)
        data = cur.fetchall()
        for rec in data:
            print(rec)


if __name__ == '__main__':
    main()
