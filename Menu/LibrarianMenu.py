from ControlSystem.LibrarianSystem import LibrianSystem

def lib_menu(back_to_menu):
    login = input("Введите логин для входа под библиотекарем - ")
    password = input("Введите пароль для входа под библиотекарем - ")

    if login != "admin" or password != "admin":
        print("Error")
        back_to_menu()
    
    librian_controller = LibrianSystem()
    print("Вы успешно вошли в систему")

    while(True):
        print("\nВыбирети функцияю\n1 - добавить новую книгу \n2 - удалить книгу из системы \n3 - зарегистрировать нового пользователя \n4 - посмотреть список всех пользователей \n5 - посмотреть список всех книг\n6 - Выйти из системы")
        choice = int(input())

        if choice == 1:
            librian_controller.add_book()
        elif choice == 2:
            librian_controller.delete_book()
        elif choice == 3:
            librian_controller.register_user()
        elif choice == 4:
            librian_controller.show_list_user()
        elif choice == 5:
            librian_controller.show_list_book()
        elif choice == 6:
            back_to_menu()
        else:
            print("Error!")
