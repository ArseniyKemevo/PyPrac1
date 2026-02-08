from Structure.PersonClass import Person

class Librarian(Person):
    def __init__(self, name):
        super().__init__(name)
    
    def get_role(self):
        return "Librarian"