class User:
    def __init__(self, first_name, last_name, email, age, country, city):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.country = country
        self.city = city
        self.attempts = 0

    def describe_user(self):
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Email: {self.email}")
        print(f"Age: {self.age}")
        print(f"Country: {self.country}")   
        print(f"City: {self.city}")

    def greet_user(self):
        print(f"Hello, {self.first_name}!")

    def login_attempts(self):
        self.attempts += 1
        print(f"login attempts: {self.attempts}")
        
    
    def reset_login_attempts(self):
        self.attempts = 0
        print(f"reset login attempts")    

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