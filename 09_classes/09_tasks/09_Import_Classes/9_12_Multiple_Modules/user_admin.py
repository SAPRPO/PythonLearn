from users_all import Admin, Priveleges
#pr = Priveleges()
#print(pr.priveleges)
print("Multiple modules test:\n")
admin = Admin('Peter', 'Petrov', 'xxx@ya.ru', 22, 'Russia', 'Moscow',  Priveleges().priveleges) # or pr.privelegies
admin.show_privelegies()
