import sqlite3

books_source = 'utils/books.db'


def create_book_table():
    con = sqlite3.connect(books_source)
    cursor = con.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS books(name text primary key,author text,read integer)")
    con.commit()
    con.close()


def add_book(name, author):
    con = sqlite3.connect(books_source)
    cursor = con.cursor()

    cursor.execute("INSERT into books VALUES(?,?,0)", (name, author))

    con.commit()
    con.close()


def book_list():
    con = sqlite3.connect(books_source)
    cursor = con.cursor()

    cursor.execute("SELECT * from books")
    books = [{'name': book[0], 'author': book[1], 'read': book[2]} for book in cursor.fetchall()]
    # fetchall() returns a list of tuples - [(name,auth,read),(name2,auth2,read2)] = each book
    # convert tuple list into a dictionary:
    # for each tuple/book(row), let [0]=name, [1] = author etc, put all those books into variable books.
    con.close()

    return books


def mark_book_as_read(read_book):
    con = sqlite3.connect(books_source)
    cursor = con.cursor()

    cursor.execute("UPDATE books SET read = 1 where name = ?", (read_book, ))

    con.commit()
    con.close()


def delete_book(unwanted_book):
    con = sqlite3.connect(books_source)
    cursor = con.cursor()

    cursor.execute("DELETE from books where name = ?", (unwanted_book, ))

    con.commit()
    con.close()
