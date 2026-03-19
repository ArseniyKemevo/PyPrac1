import os
import pickle
from config import user_list, book_list

class FileSystem:
    def __init__(self, book_file="books.pkl", user_file="users.pkl"):
        self.book_file = book_file
        self.user_file = user_file

    def load_books(self):
        if os.path.exists(self.book_file):
            with open(self.book_file, "rb") as f:
                return pickle.load(f)
        return []

    def load_users(self):
        if os.path.exists(self.user_file):
            with open(self.user_file, "rb") as f:
                return pickle.load(f)
        return []

    def save_books(self):
        with open(self.book_file, "wb") as f:
            pickle.dump(book_list, f)

    def save_users(self):
        with open(self.user_file, "wb") as f:
            pickle.dump(user_list, f)