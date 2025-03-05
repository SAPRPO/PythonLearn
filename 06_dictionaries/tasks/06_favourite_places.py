

person1={'first_name' : 'Ivan',
        'last_name' : 'Ivanov',
        'age' : '20',
        'city' : 'Moscow',
        }

person2={'first_name' : 'Petr',
        'last_name' : 'Petrov',
        'age' : '21',
        'city' : 'Omsk',
        }
person3={'first_name' : 'Alex',
        'last_name' : 'Sidorov',
        'age' : '22',
        'city' : 'Tomsk',
        }


favourite_places={'Moscow' : [person1, person2],
                  'Spb' : [person2],
                  'Village': [person1,person2,person3]}

for key,values in favourite_places.items():
    print("\n"+key+" is favourite place for:")
    for value in values:
        print("\t"+value['first_name']+" "+value['last_name']+" "+value['age']+" "+value['city'])

