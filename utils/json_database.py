import json
books_source = 'utils/books.json'


def create_book_file():                 # To create blank file/ make sure file exists and make sure its NOT empty
    with open(books_source, 'a') as file:
        json.dump([], file)                     # put an empty list (json file cant be empty


def add_book(name, author):
    books = book_list()
    books.append({'name': name, 'author': author, 'read': False})
    _save_all_books(books)


def book_list():
    with open(books_source, 'r') as file:
        return json.load(file)


def _save_all_books(books):
    with open(books_source, 'w') as file:
        json.dump(books, file)


def mark_book_as_read(read_book):
    books = book_list()
    for book in books:
        if book['name'] == read_book:
            book['read'] = True
    _save_all_books(books)


def delete_book(unwanted_book):
    books = book_list()
    books = [book for book in books if book['name'] != unwanted_book]   # put book into list if name isn't unwanted_book
    _save_all_books(books)