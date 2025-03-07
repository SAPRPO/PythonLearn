def build_person(first_name, last_name, age=''):
    person = {'first' : first_name, 'last' : last_name}
    if age:
        person['age'] = age #add age
    return person
musician =build_person('mille','petrozza', age=55)
print(musician)