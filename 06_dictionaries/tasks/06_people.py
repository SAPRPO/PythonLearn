person1={'first_name' : 'Ivan',
        'last_name' : 'Ivanov',
        'age' : '20',
        'city' : 'Moscow'
        }

person2={'first_name' : 'Petr',
        'last_name' : 'Petrov',
        'age' : '21',
        'city' : 'Omsk'
        }
person3={'first_name' : 'Alex',
        'last_name' : 'Sidorov',
        'age' : '22',
        'city' : 'Tomsk'
        }

print('...')
people=[person1,person2,person3]
for person in people:
    print(person)
print('...')

for person in people:
    print(person['first_name'],person['last_name'],person['age'],person['city'])