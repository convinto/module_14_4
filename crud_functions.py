import sqlite3
from distutils.command.check import check

def initiate_db():
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INT,
    title TEXT NOT NULL,
    description TEXT,
    price INT NOT NULL
    )
    ''')
    connection.commit()
    connection.close()

def get_all_products():
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM Products")
    users = cursor.fetchall()

    connection.commit()
    connection.close()
    return users



#пополнение на 4 записи
# for i in range(1, 5):
#     cursor.execute("INSERT INTO Products (id, title, description, price) VALUES (?, ?, ?, ?)", (f'{i}', f"Product{i}", f"description{i}", 1000))

