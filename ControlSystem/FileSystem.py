import os
from Structure.BookClass import Book
from Structure.UserClass import User
from config import user_list, book_list

class FileSystem:
    def __init__(self, book_file="books.txt", user_file="users.txt"):
        self.book_file = book_file
        self.user_file = user_file

    def load_books(self):
        books = []
        if os.path.exists(self.book_file):
            with open(self.book_file, "r", encoding="utf-8") as f:
                for line in f:
                    parts = line.strip().split("|")
                    if len(parts) == 3:
                        name, author, status_str = parts
                        status = status_str == "available"
                        books.append(Book(name, author, status))
        return books

    def load_users(self, books_list):
        users = []
        if os.path.exists(self.user_file):
            with open(self.user_file, "r", encoding="utf-8") as f:
                for line in f:
                    parts = line.strip().split("|")
                    if len(parts) == 2:
                        name, books_str = parts
                        user = User(name)
                        if books_str:
                            for book_name in books_str.split(","):
                                book_obj = next((b for b in books_list if b.get_name() == book_name), None)
                                if book_obj:
                                    user.add_book(book_obj)
                        users.append(user)
        return users

    def save_books(self):
        with open(self.book_file, "w", encoding="utf-8") as f:
            for book in book_list:
                status_str = "available" if book.get_status() else "taken"
                f.write(f"{book.get_name()}|{book.get_author()}|{status_str}\n")

    def save_users(self):
        with open(self.user_file, "w", encoding="utf-8") as f:
            for user in user_list:
                books_str = ",".join([b.get_name() for b in user.get_books()])
                f.write(f"{user.get_name()}|{books_str}\n")

    