import os
import pickle
from config import user_list, book_list

class FileSystem:
    def __init__(self, data_file="data.pkl"):
        self.data_file = data_file

    def load_data(self):
        if os.path.exists(self.data_file):
            with open(self.data_file, "rb") as f:
                data = pickle.load(f)
                return data.get("books", []), data.get("users", [])
        
        return [], []

    def save_data(self):
        with open(self.data_file, "wb") as f:
            data = {
                "books": book_list,
                "users": user_list
            }
            pickle.dump(data, f)