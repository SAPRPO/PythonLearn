#conditional tests

string1='test'
string2='test'

if string1==string2:
    print(string1==string2) #True
else:
    print(string1==string2) #False

print('using lower')
cars=['bmw','audi','toyota', 'subaru','honda']
car = 'BMW'
if (car.lower() == cars[0]):
    print(car.lower() == cars[0]) #True

print('\n> < >= <=\n')

x = 8
if x > 5:
    print(f'{x} is greater than 5')
    if x > 7:
       print(f'{x} is greater than 7')
       if x < 10 and x==9:
            print(f'{x} is less than 10 and x is 9')
       else:
           print(f'{x} is less than 10 and x is not 9')

c = 'honda s2000'
if (c in cars):
    print(f'{c} is in cars list')
else:
    print(f'{c} is not in cars list')