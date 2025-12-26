import database
from fastapi import FastAPI
from database import get_connection

app = FastAPI()

conn = get_connection()

# Book Management Endpoints
@app.get("/books")
def get_books():
    books_list = []
    database.c.execute("SELECT * FROM books")
    database.con.commit()
    books = database.c.fetchall()
    for book in books:
        books_list.append({
            "id": book[0],
            "title": book[1],
            "reg_no": book[2],
            "availability": book[3]
        })
    return books_list

@app.get("/books/{book_id}")
def get_book(book_id: int):
    database.c.execute("SELECT * FROM books WHERE id=?", (book_id,))
    database.con.commit()
    book = database.c.fetchone()
    if book:
        return {
            "id": book[0],
            "title": book[1],
            "reg_no": book[2],
            "availability": book[3]
        }
    return {"Error": "Book not found"}

@app.post("/books")
def add_book(title: str, reg_no: str, availability: str):
    database.c.execute("INSERT INTO books (title, reg_no, availability) VALUES (?, ?, ?)",
                       (title, reg_no, availability))
    database.con.commit()
    return {"Message": "Book added successfully"}

@app.put("/books/{book_id}")
def update_book(book_id: int, title: str | None = None, reg_no: str | None = None, availability: str | None = None):
    if title:
        database.c.execute("UPDATE books SET title=? WHERE id=?", (title, book_id))
    if reg_no:
        database.c.execute("UPDATE books SET reg_no=? WHERE id=?", (reg_no, book_id))
    if availability:
        database.c.execute("UPDATE books SET availability=? WHERE id=?", (availability, book_id))
    database.con.commit()
    return {"Message": "Book updated successfully"}

@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    database.c.execute("DELETE FROM books WHERE id=?", (book_id,))
    database.con.commit()
    return {"Message": "Book deleted successfully"}

# Member Management Endpoints

@app.get("/members")
def get_members():
    members_list = []
    database.c.execute("SELECT * FROM members")
    database.con.commit()
    members = database.c.fetchall()
    for member in members:
        members_list.append({
            "id": member[0],
            "name": member[1],
            "email": member[2]
        })
    return members_list

@app.post("/members")
def add_member(name: str, email: str):
    database.c.execute("INSERT INTO members (name, email) VALUES (?, ?)",
                       (name, email))
    database.con.commit()
    return {"Message": "Member added successfully"}

@app.put("/members/{member_id}")
def update_member(member_id: int, name: str | None = None, email: str | None = None):
    if name:
        database.c.execute("UPDATE members SET name=? WHERE id=?", (name, member_id))
    if email:
        database.c.execute("UPDATE members SET email=? WHERE id=?", (email, member_id))
    database.con.commit()
    return {"Message": "Member updated successfully"}

@app.delete("/members/{member_id}")
def delete_member(member_id: int):
    database.c.execute("SELECT * From BORROW_RECORDS WHERE member_id=?", (member_id,))
    records = database.c.fetchall()
    if records:
        return {"Error": "Cannot delete member with active borrow records"}
    else:
       database.c.execute("DELETE FROM members WHERE id=?", (member_id,))
       database.con.commit()
       return {"Message": "Member deleted successfully"}
    
@app.post("/borrow")
def borrow_book(book_id: int, member_id: int, borrow_date: str):
    database.c.execute("SELECT availability FROM books WHERE id=?", (book_id,))
    book = database.c.fetchone()
    if book and book[0] == "available":
        database.c.execute("INSERT INTO borrow_records (book_id, member_id, borrow_date) VALUES (?, ?, ?)",
                           (book_id, member_id, borrow_date))
        database.c.execute("UPDATE books SET availability='Unavailable' WHERE id=?", (book_id,))
        database.con.commit()
        return {"Message": "Book borrowed successfully"}
    return {"Error": "Book is not available"}
    
@app.put("/return")
def return_book(book_id: int, member_id: int, return_date: str):    
    database.c.execute("SELECT * FROM borrow_records WHERE book_id=? AND member_id=? AND return_date IS NULL",
                       (book_id, member_id))
    record = database.c.fetchone()
    if record:
        database.c.execute("UPDATE borrow_records SET return_date=? WHERE book_id=? AND member_id=? AND return_date IS NULL",
                           (return_date, book_id, member_id))
        database.c.execute("UPDATE books SET availability='available' WHERE id=?", (book_id,))
        database.con.commit()
        return {"Message": "Book returned successfully"}
    return {"Error": "No active borrow record found for this book and member"}

@app.get("/borrow_records")
def get_borrow_records():
    records_list = []
    database.c.execute("SELECT * FROM borrow_records")
    database.con.commit()
    records = database.c.fetchall()
    for record in records:
        records_list.append({
            "id": record[0],
            "book_id": record[1],
            "member_id": record[2],
            "borrow_date": record[3],
            "return_date": record[4]
        })
    return records_list

@app.get("/borrow_records/{record_id}")
def get_borrow_record(record_id: int):
    database.c.execute("SELECT * FROM borrow_records WHERE id=?", (record_id,))
    database.con.commit()
    record = database.c.fetchone()
    if record:
        return {
            "id": record[0],
            "book_id": record[1],
            "member_id": record[2],
            "borrow_date": record[3],
            "return_date": record[4]
        }
    return {"Error": "Borrow record not found"}

@app.get("/books/search/title/{book_title}")
def search_books(book_title: str):
    books_list = []
    title_query = f"%{book_title}%"
    database.c.execute("SELECT * FROM books WHERE title LIKE ?", (title_query,))
    database.con.commit()
    books = database.c.fetchall()
    for book in books:
        books_list.append({
            "id": book[0],
            "title": book[1],
            "reg_no": book[2],
            "availability": book[3]
        })
    return books_list