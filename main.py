from Menu.MainMenu import menu
from ControlSystem.FileSystem import FileSystem
from config import book_list, user_list 

def main():
    fs = FileSystem()

    book_list.clear()
    user_list.clear()

    loaded_books, loaded_users = fs.load_data()
    book_list.extend(loaded_books)
    user_list.extend(loaded_users)

    menu()

if __name__ == "__main__":
    main()