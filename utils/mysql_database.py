import mysql.connector as mysql


def create_book_table():
    con = mysql.connect(host='localhost', auth_plugin='mysql_native_password', database='prac',
                        user='adrianoqpchikande', password='0000')
    cursor = con.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS books(name text,author text,used integer)")
    con.commit()
    con.close()


def add_book(name, author):
    con = mysql.connect(host='localhost', auth_plugin='mysql_native_password', database='prac',
                        user='adrianoqpchikande', password='0000')
    cursor = con.cursor()

    cursor.execute("INSERT into prac.books VALUES(%s,%s,0)", (name, author))
    print(f"{name.title()} successfully added, returning to library menu....")
    con.commit()
    con.close()


def book_list():
    con = mysql.connect(host='localhost', auth_plugin='mysql_native_password', database='prac',
                        user='adrianoqpchikande', password='0000')
    cursor = con.cursor()

    cursor.execute("SELECT * from prac.books")
    books = [{'name': book[0], 'author': book[1], 'read': book[2]} for book in cursor.fetchall()]
    # fetchall() returns a list of tuples - [(name,auth,read),(name2,auth2,read2)] = each book
    # convert tuple list into a dictionary:
    # for each tuple/book(row), let [0]=name, [1] = author etc, put all those books into variable books.
    con.close()

    return books


def mark_book_as_read(read_book):
    con = mysql.connect(host='localhost', auth_plugin='mysql_native_password', database='prac',
                        user='adrianoqpchikande', password='0000')
    cursor = con.cursor()

    cursor.execute("UPDATE prac.books SET used = 1 where name = %s", (read_book, ))

    con.commit()
    con.close()


def delete_book(unwanted_book):
    con = mysql.connect(host='localhost', auth_plugin='mysql_native_password', database='prac',
                        user='adrianoqpchikande', password='0000')
    cursor = con.cursor()

    cursor.execute("DELETE from prac.books where name = %s", (unwanted_book, ))

    con.commit()
    con.close()
