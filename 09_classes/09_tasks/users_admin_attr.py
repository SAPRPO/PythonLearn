from users_class import User
from priveleges import Priveleges



class Admin(User):
    def __init__(self, first_name, last_name, email, age, country, city, priveleges):
        super().__init__(first_name, last_name, email, age, country, city)
        self.priveleges = Priveleges()


admin = Admin("Ivan", "Ivanov", "trololo@yandex.ru", 25, "Russia", "Moscow", priveleges=[])
admin.priveleges