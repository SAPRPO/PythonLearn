from user import User
class Admin(User):
    def __init__(self, first_name, last_name, email, age, country, city, priveleges):
        super().__init__(first_name, last_name, email, age, country, city)
        self.priveleges = priveleges
    
    def show_privelegies(self):
        print("Admin's privelegies: ")
        for p in self.priveleges:
            print(p)

class Priveleges:
    def __init__(self, priveleges = ['Разрешено добавлять сообщения','Разрешено удалять пользователей','Разрешено банить пользователей']):
    #def __init__(self, priveleges = []):
        self.priveleges = priveleges
    
    def show_priveleges(self):
        print("Admin's privelegies: ")
        for p in self.priveleges:
            print(p)