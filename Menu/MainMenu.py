from Menu.LibrarianMenu import lib_menu
from Menu.UserMenu import user_menu
from ControlSystem.FileSystem import FileSystem
import sys

def menu():
    fs = FileSystem()

    print("\nПривет, под какой ролью вы хотите войти в систему?\n1 - Библиотекарь \n2 - Пользователь \n3 - Выйти")
    choise = int(input("Ваш выбор: "))

    if choise == 1:
        lib_menu(menu)
    elif choise == 2:
        user_menu(menu)
    elif choise == 3:
        fs.save_books()
        fs.save_users()
        print("Данные сохранены. Программа завершена.")
        sys.exit()
    else:
        print("Ошибка! Неверный ввод.")
        menu()