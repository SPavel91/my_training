import sqlite3

def initiate_db():
    connection = sqlite3.connect("Products.db")
    cursor = connection.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INTEGER NOT NULL)
    ''')
    # for i in range(1, 5):
    #    cursor.execute("INSERT INTO Products (title, description, price) VALUES (?, ?, ?)", (f"Product{i}", f"описание{i}", i * 10))
    connection.commit()
    connection.close()

    connection = sqlite3.connect("Users.db")
    cursor1 = connection.cursor()
    cursor1.execute('''
    CREATE TABLE IF NOT EXISTS Users(
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL ,
    email TEXT NOT NULL,
    age INTEGER NOT NULL,
    balance INTEGER NOT NULL)
    ''')
    connection.commit()
    connection.close()


def get_all_products():
    connection = sqlite3.connect('Products.db')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Products")
    products = cursor.fetchall()
    cursor.close()
    connection.close()
    return products


def add_user(username, email, age):
    connection = sqlite3.connect("Users.db")
    cursor1 = connection.cursor()
    cursor1.execute("INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)",
                   (username, email, age, 1000))
    connection.commit()
    connection.close()


def is_included(username):
    connection = sqlite3.connect("Users.db")
    cursor1 = connection.cursor()
    cursor1.execute("SELECT * FROM Users WHERE username = ?", (username,))
    check_user = cursor1.fetchone()
    cursor1.close()
    connection.close()
    if check_user is None:
        return False
    else:
        return True