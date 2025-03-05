barsik={'animal' : 'cat',
       'owner' : 'michael',
    }
jacoby={'animal':'bird',
        'owner':'anton'}

jimmy={'animal':'dog',
        'owner':'peter'}
    
pets=[barsik,jacoby,jimmy]

count =1 
for pet in pets:
    print(f'{count} pet: ')
    count = count +1
    for key,value in pet.items():
        print(f'\t{key.title()} : {value.title()}')