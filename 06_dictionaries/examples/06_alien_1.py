alien_0 = {'colour': 'green', 'points':5} #dictionary

print(alien_0['colour']) #return value
print(alien_0['points'])

new_points=alien_0['points']
print(f"You just earned {new_points} points")

# add new pairs key-value

alien_0['x_position'] = 0
alien_0['y_position'] = 25

print(alien_0)

print("\nCreate empty dictionary:\n")
alien_0 = {}
alien_0['colour'] = 'green'
alien_0['points'] = 5

print(alien_0)
print("\nChange values in dictionary:\n")

alien_0 = {'colour': 'green'}
print(f"Alien colour is {alien_0['colour']}")
alien_0['colour'] = 'yellow' #change value
print(f"Alien colour is now {alien_0['colour']}")