
def describe_pet_s(animal_type, pet_name):
    print(f'I have a {animal_type}')
    print(f"My {animal_type}'s name is {pet_name.title()}\n")

def describe_pet(pet_name, animal_type = 'dog'):
    print(f'I have a {animal_type}')
    print(f"My {animal_type}'s name is {pet_name.title()}\n")

#position arguments

describe_pet_s('dog', 'sharik')
describe_pet_s('parrot', 'Jacob')

#named_arguments
describe_pet(animal_type= 'lizard', pet_name= 'Js')

#default_value , use named argumets for both parameters, not for one

describe_pet(pet_name='rex')

#equal calls

describe_pet("KK")
describe_pet(pet_name='willy')
describe_pet(pet_name='bars', animal_type='cat')
describe_pet(animal_type='cat', pet_name='bars')