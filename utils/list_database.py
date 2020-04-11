books = []


def add_book(name, author):
    new_book = {'name': name, 'author': author, 'read': False}
    books.append(new_book)
    print("Book Added, Returning to Main Menu.......")


def book_list():
    return books


def mark_book_as_read(read_book):

    for book in books:
        if book['name'] == read_book:
            book['read'] = True


# region Delete Book v1
# Bad practice to modify lists while iterating through them


# def delete_book(unwanted):
#     for book in books:
#         if book['name'] == unwanted:
#             del books[book]             # books.remove(book)
#             print("Book deleted")
#         else:
#             print("Book not found")
# endregion


def delete_book(unwanted_book):
    global books
    books = [book for book in books if book['name'] != unwanted_book]
