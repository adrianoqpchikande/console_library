books_source = 'utils/books.txt'


def create_book_file():                 # Just to create blank file/ make sure file exists
    with open(books_source, 'a'):
        pass


def add_book(name, author):
    with open(books_source, 'a') as file:                      # 'a' appends to file ie adds instead of overwriting
        file.write(f"{name},{author},0\n")
    print("Book Added, Returning to Main Menu.......")


def book_list():
    with open(books_source, 'r') as file:
        lines = [line.strip().split(',') for line in file.readlines()]  # split produces a list of book lists

    books = [   # [[name,author,read],[name2,auth2,read],[name3,auth3,read]]
        {'name': line[0], 'author': line[1], 'read': line[2]}
        for line in lines]
    return books


def mark_book_as_read(read_book):
    books = book_list()
    for book in books:
        if book['name'] == read_book:
            book['read'] = '1'
    _save_all_books(books)


def _save_all_books(books):  # _ to tell other users not to call this Fn ie private Fn, use only in this file
    with open(books_source, 'w') as file:
        for book in books:
            file.write(f"{book['name']},{book['author']},{book['read']}\n")
    

def delete_book(unwanted_book):
    books = book_list()
    books = [book for book in books if book['name'] != unwanted_book]   # put book into list if name isn't unwanted_book
    _save_all_books(books)