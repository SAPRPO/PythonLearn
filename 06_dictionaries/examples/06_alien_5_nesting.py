alien_0 = {'color': 'green', 'points': 5}
alien_l = {'color': 'yellow', 'points': 10}
alien_2 = {'color' : 'red', 'points' : 15}

aliens_test = [alien_0, alien_l, alien_2]

for alien in aliens_test:
    print(alien)

aliens = []
#add 30 aliens to the list
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)
#first five aliens
for alien in aliens[:5]:
    print(alien)

print("...")
print(f"Total number of aliens: {len(aliens)}")
print("..............................................")
#empty list to store aliens
aliens =[]

#make 30 aliens
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[:3]:
    if alien['color'] =='green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15

for alien in aliens[:5]:
    print(alien)

for alien in aliens[:10]:
    if alien['color'] =='green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15

for alien in aliens[:10]:
    print(alien)

    