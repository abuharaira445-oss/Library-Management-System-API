import sqlite3

def get_connection():
    return sqlite3.connect('database.db', check_same_thread=False)
con = sqlite3.connect('database.db', check_same_thread=False)
c = con.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS books
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
              title TEXT NOT NULL,
              reg_no TEXT NOT NULL,
              availability TEXT NOT NULL)''')
con.commit()
c.execute('''CREATE TABLE IF NOT EXISTS members
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL)''')
con.commit()
c.execute('''CREATE TABLE IF NOT EXISTS borrow_records
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                book_id INTEGER NOT NULL,
                member_id INTEGER NOT NULL,
                borrow_date TEXT NOT NULL,
                return_date TEXT,
                FOREIGN KEY(book_id) REFERENCES books(id),
                FOREIGN KEY(member_id) REFERENCES members(id))''')