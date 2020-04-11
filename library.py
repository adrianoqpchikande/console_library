from utils import mysql_database


user_choice = """
-'a' to Add a Book
-'l' to View Book List
-'r' to Mark a Book as Read
-'d' to Delete a Book
-'q' to Quit Application

What do you want to do: """


def lib_menu():
    mysql_database.create_book_table()
    user_input = input(user_choice)

    while user_input != 'q'.lower():
        if user_input == 'a':
            prompt_add_book()
        elif user_input == 'l':
            print("\n")
            prompt_list_books()
        elif user_input == 'r':
            prompt_mark_as_read()
        elif user_input == 'd':
            prompt_delete_book()
        else:
            print("Invalid Option, Try again")
        user_input = input(user_choice)

    if user_input == 'q':
        print("Exiting....")


def prompt_add_book():
    name = input("Enter title of book: ")
    author = input("Enter name of author: ")
    mysql_database.add_book(name, author)


def prompt_list_books():
    book_list = mysql_database.book_list()
    if not book_list:
        print("No books found")
    for i in book_list:
        r = "Read" if i['read'] else "Not yet Read"
        print(f"{i['name']} by {i['author']}, {r}")


def prompt_mark_as_read():
    read_book = input("Enter title of book you just read: ")
    mysql_database.mark_book_as_read(read_book)


def prompt_delete_book():
    unwanted_book = input("Enter title of book you want to delete: ")
    mysql_database.delete_book(unwanted_book)


# lib_menu()
