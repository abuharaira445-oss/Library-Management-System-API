from pydantic import BaseModel
from datetime import date

class Book(BaseModel):
    id: int
    title: str
    reg_no: str
    availability: str

class Member(BaseModel):
    id: int
    name: str
    email: str

class BorrowRecord(BaseModel):
    id: int
    book_id: int
    member_id: int
    borrow_date: date
    return_date: date