from config import user_list
from ControlSystem.UserSystem import UserSystem

def user_menu(back_to_menu):
    name_user = input("Введите имя - ")
    current_user = None

    for user in user_list:
        if user.get_name().lower() == name_user.lower():
            current_user = user
            break

    if current_user is None:
        print("Пользователь с таким именем не найден")
        back_to_menu()
    else:
        print("Вы успешно вошли в систему")
        user_controller = UserSystem(current_user)

        while(True):
            print("\n1 - Посмотреть доступные книги\n2 - Взять книгу \n3 - Вернуть книгу \n4 - Посмотреть мои книги \n5 - Выйти")

            choice = int(input())

            if choice == 1:
                user_controller.show_availble_books()
            elif choice == 2:
                user_controller.take_book()
            elif choice == 3:
                user_controller.return_book()
            elif choice == 4:
                user_controller.show_my_books()
            elif choice == 5:
                back_to_menu()
            else:
                print("Error")