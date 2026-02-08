from config import book_list, user_list
from Structure.BookClass import Book
from Structure.UserClass import User

class LibrianSystem():
    def __init__(self):
        pass

    def add_book(self):
        name = input("Введити название книги - ")
        author = input("Введите имя автора - ")

        book_list.append(Book(name, author))

        print("Книга добавлена!")
    
    def delete_book(self):
        name = input("Введите название книги, которую хотите удалить - ")
        
        for book in book_list:
            if book.get_name().lower() == name.lower():
                book_list.remove(book)
                print("Книга удалена")
                return
            
        print("Книга не найдена")
    
    def register_user(self):
        name = input("Введите имя нового пользователя - ")

        for user in user_list:
            if user.get_name().lower() == name.lower():
                print("Такой пользователь уже существует")
                return

        user_list.append(User(name))
        print("Пользователь зарегистрирован")
    
    def show_list_user(self):
        if len(user_list) == 0:
            print("Пользователей нет")
            return

        for user in user_list:
            print(f"Имя пользователя: {user.get_name()}")
    
    def show_list_book(self):
        if len(book_list) == 0:
            print("Список пуст")
            return
        
        for book in book_list:
            print(f"Название - {book.get_name()}, Автор - {book.get_author()}, Статус свободна(да\нет) - {book.get_status()}")