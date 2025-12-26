# Library Management System API

A RESTful Library Management System API built using Python, FastAPI, and SQLite.
This project allows managing books, members, and borrowing records, including availability tracking and search functionality.

# Features

* Manage books (add, view, update, delete)
* Manage library members
* Borrow and return books
* Track book availability
* Search books by title and author
* SQLite database for persistent storage
* Interactive API documentation (Swagger UI)

# Tech Stack

* Python
* FastAPI
* SQLite
* Pydantic
* Uvicorn

---

# Project Structure

library-api/
│
├── main.py          # FastAPI app & routes
├── database.py      # SQLite connection & queries
├── models.py        # Pydantic models
├── library.db       # SQLite database
├── requirements.txt
└── README.md

# 🗄 Database Tables

# Books

* id (INTEGER, PK)
* title (TEXT)
* author (TEXT)
* reg_no (TEXT)
* availability (TEXT)

# Members

* id (INTEGER, PK)
* name (TEXT)
* email (TEXT)

# Borrow Records

* id (INTEGER, PK)
* book_id (FK)
* member_id (FK)
* borrow_date (TEXT)
* return_date (TEXT)

# API Endpoints

# Books

| Method | Endpoint                         | Description     |
| ------ | -------------------------------- | --------------- |
| GET    | /books                           | Get all books   |
| GET    | /books/{book_id}                 | Get book by ID  |
| POST   | /books                           | Add a new book  |       |
| PUT    | /books/{book_id}                 | Update book     |
| DELETE | /books/{book_id}                 | Delete book     |
| GET    | /books/search/title/{book_title} | Search by title |

# Members

| Method | Endpoint             | Description     |
| ------ | -------------------- | --------------- |
| GET    | /members             | Get all members |
| POST   | /members             | Add member      |
| DELETE | /members/{member_id} | Delete member   |

# Borrowing

| Method | Endpoint          | Description         |
| ------ | ----------------- | ------------------- |
| POST   | /borrow           | Borrow a book       |
| POST   | /return           | Return a book       |
| GET    | /borrow_records   | View borrowed books |

---

# Example Request (Borrow Book)

{
  "book_id": 1,
  "member_id": 2,
  "borrow_date": "2025-01-10",
  "return_date": "2025-01-20"
}

# How to Run the Project

# Clone the repository

git clone https://github.com/your-username/library-api.git
cd library-api

# Create virtual environment

python -m venv venv
venv\Scripts\activate   # Windows

# Install dependencies

pip install -r requirements.txt

# Run the server

uvicorn main:app --reload

# Open Swagger UI

[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

# Purpose

This project is designed to:

* Practice FastAPI backend development
* Understand SQLite relationships & queries
* Implement real-world CRUD operations
* Learn API-based data validation using Pydantic

# Author

Abu Huraira
Backend development with Python & FastAPI
