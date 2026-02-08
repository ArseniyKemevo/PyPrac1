class Book():
    def __init__(self, name_book, author, status = True):
        self._name_book = name_book
        self._author = author
        self._status = status

    def get_name(self):
        return self._name_book

    def get_author(self):
        return self._author

    def get_status(self):
        return self._status

    def set_status(self, status):
        self._status = status