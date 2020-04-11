import mysql.connector as mysql

import library

user_choice = """
-'l' to login
-'r' to register
-'q' to quit
What do you want to do: """


def log_menu():
    user_input = input(user_choice)

    while user_input != 'q':
        if user_input == 'l':
            login()
            break
        elif user_input == 'r':
            register()
        else:
            print("Invalid input, try again.")
        user_input = input(user_choice)


# region Login v1
# def login():
#     print("Welcome, please enter your username and password")
#     user_name = input("Username: ")
#     password = input("Password: ")
#
#     b = True        # Allow user to enter login credentials until they are correct
#     while b:
#         # Connect to database
#         con = mysql.connect(host='localhost', auth_plugin='mysql_native_password', database='prac',
#                             user='adrianoqpchikande', password='0000')
#         cursor = con.cursor()
#         cursor.execute("SELECT * from prac.users")
#
#         # Retrieve users from database = list of dicts
#         users = [{'name': users[0], 'password': users[1]} for users in cursor.fetchall()]
#
#         # Validate entered login credentials
#         for user in users:                              # Loop through all users
#             if user['name'] == user_name and user['password'] == password:
#                 library.lib_menu()
#                 b = False                               # Will allow to break out of while loop
#
#         if b:                                           # b will be false if wrong credentials are entered
#             print("Wrong login credentials")
#             user_name = input("Username: ")             # Re-enter login credentials
#             password = input("Password: ")
#         else:
#             print("Exiting")           # After successful login and activity, b=false = break out of while loop
#             con.commit()
#             con.close()
# endregion

# region Login v2
def login():

    print("Welcome, please enter your username and password ")

    b = True       # Allow user to enter login credentials until they are correct
    while b:
        user_name = input("Username: ")
        password = input("Password: ")

        # Connect to database
        con = mysql.connect(host='localhost', auth_plugin='mysql_native_password', database='prac',
                            user='adrianoqpchikande', password='0000')
        cursor = con.cursor()
        cursor.execute("SELECT * from prac.users where name=%s and password=%s", (user_name, password))
        cursor.fetchall()

        if cursor.rowcount == 1:
            b = False
            library.lib_menu()
        else:
            print("Wrong login credentials, Please try again\n")

# endregion


def register():
    print("Welcome, please enter your new username and password")
    user_name = input("Username: ")

    # Connect to database
    con = mysql.connect(host='localhost', auth_plugin='mysql_native_password', database='prac',
                        user='adrianoqpchikande', password='0000')
    cursor = con.cursor()

    # Check if supplied username already exists
    cursor.execute("SELECT name from prac.users")
    user_names = []
    for users in cursor.fetchall():
        a = users[0]
        user_names.append(a)

    while user_name in user_names:
        print("Username already exists, please try again")
        user_name = input("Username: ")

    # Proceed to ask for pass word if username does not exist in database and register new user into database
    password = input("Password: ")
    cursor.execute("INSERT into prac.users VALUES(%s,%s)", (user_name, password))
    con.commit()
    con.close()
    print(f"\n{user_name.title()} registered, now returning to main menu..............")


log_menu()
