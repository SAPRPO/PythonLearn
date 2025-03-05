favourite_digits={
    'Ivan' : [1, 5,6,3],
    'Alex' : [2,7,3,767,22],
    'Anna' : [7, 8, 666, 888 ],
    'Max'  : [9 , 1488,33,11],
}
count = 1

for name, digits in favourite_digits.items(): 
    print(f'{count}. Name: {name}. favourite digits: ')
    count +=1
    for d in digits:
        print(d)
    print('\n')