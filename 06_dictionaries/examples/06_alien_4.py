alien_0 = {'color': 'green', 'speed': 'slow',}
#print(alien_0['points'])

point_value =alien_0.get('points', 'No point value assigned') #key, if no key return value (text)
print(point_value)