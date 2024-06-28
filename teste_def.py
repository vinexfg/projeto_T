

class Pessoa:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    def of_legal_age(self):
        if self.age >= 18:
            return True
        else:
            return False
        
        