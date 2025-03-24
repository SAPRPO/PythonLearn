class Priveleges:
    def __init__(self, priveleges = ['Разрешено добавлять сообщения','Разрешено удалять пользователей','Разрешено банить пользователей']):
    #def __init__(self, priveleges = []):
        self.priveleges = priveleges
    
    def show_priveleges(self):
        print("Admin's privelegies: ")
        for p in self.priveleges:
            print(p)