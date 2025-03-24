from users_class import User

class Priveleges:
    def __init__(self, priveleges):
        self.priveleges =priveleges
    
    def show_priveleges(self):
        print("Admin's privelegies: ")
        for p in self.priveleges:
            print(p)

class Admin(User):
    def __init__(self, first_name, last_name, email, age, country, city, priveleges):
        super().__init__(first_name, last_name, email, age, country, city)
        self.priveleges = priveleges
    
    def show_privelegies(self):
        print("Admin's privelegies: ")
        for p in self.priveleges:
            print(p)

    #message1 = "Разрешено добавлять сообщения"
    #message2 = "Разрешено удалять пользователей"
    #message3 = "Разрешено банить пользователей"

admin = Admin("Ivan", "Ivanov", "trololo@yandex.ru", 25, "Russia", "Moscow", ['Разрешено добавлять сообщения', 'Разрешено удалять пользователей', 'Разрешено банить пользователей'])
admin.show_privelegies()