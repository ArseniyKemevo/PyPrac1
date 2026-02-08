from Structure.PersonClass import Person
from Structure.BookClass import Book

class User(Person):
    def __init__(self, name):
        super().__init__(name)
        self._books = []
    
    def get_role(self):
        return "User"
    
    def add_book(self, name_book : Book):
        self._books.append(name_book)

    def remove_book(self, name_book : Book):
        if name_book in self._books:
            self._books.remove(name_book)

    def get_books(self):
        return self._books
