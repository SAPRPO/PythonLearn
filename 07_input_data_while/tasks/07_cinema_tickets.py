
while True:
    mes = input("Enter your age: ")
    if mes.isdigit() == False:
        print('Bad value!')
        continue
    if mes == "quit":
        break
    visitor_age = int(mes)
    if visitor_age <3:
        print(f"If your age {visitor_age} Your ticket is free")
    if visitor_age >=3 and visitor_age <=12:
        print(f"If your age {visitor_age} Your ticket price is $10")
    if visitor_age >12:
        print(f"If your age {visitor_age} Your ticket price is $15")
    
# visiors ,price , summ