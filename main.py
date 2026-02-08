from Menu.MainMenu import menu
from ControlSystem.FileSystem import FileSystem
from config import book_list, user_list 

def main():
    fs = FileSystem()

    book_list.extend(fs.load_books())
    user_list.extend(fs.load_users(book_list))

    menu()

if __name__ == "__main__":
    main()
