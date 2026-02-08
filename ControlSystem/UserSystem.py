from config import book_list, user_list
from Structure.UserClass import User

class UserSystem():
    def __init__(self, user : User):
        self.user = user

    def show_availble_books(self):
        if len(book_list) == 0:
            print("Список пуст")
            return

        for book in book_list:
            if book.get_status():
                print(f"{book.get_name()} {book.get_author()}")

    def take_book(self):
        name_book = input("Введите название книги, которую хотите взять - ")

        for book in book_list:
            if book.get_name().lower() == name_book.lower():
                if book.get_status():
                    book.set_status(False)
                    self.user.add_book(book)
                    print("Книга получена")
                    return
                else:
                    print("Нельзя получить данную книгу")
                    return
            
        print("Книга не найдена")

    def return_book(self):
        name_book = input("Введите название книги, которую хотите вернуть - ")

        for book in book_list:
            if book.get_name().lower() == name_book.lower():
                if name_book in self.user.get_books():
                    book.set_status(True)
                    self.user.remove_book(book)
                    print("Книга успешно возвращена")
                    return
                else:
                    print("Вы не брали эту книгу")
                    return
                
        print("Книга не найдена")

    def show_my_books(self):
        books = self.user.get_books()
        if not books:
            print("Пользователь не брал книги")
        else:
            for book in books:
                print(f"\nСписок книг, которые взял пользователь\nНазвание - {book.get_name()}, Автор - {book.get_author()}")

    