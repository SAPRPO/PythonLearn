citylist = ['Volgograd', 'Novgorod', 'Pskov', 'Moscow', 'Saint-Petesburg', 'Samara', 'Kaluga' ]
print(citylist)

print('\nsorted\n')
print(sorted(citylist))

print('\nsorted reverse\n')
print(sorted(citylist, reverse=True))
#length
length=len(citylist)
print(f"citylist has {length} elements")
citylist.insert(0, 'Vladimir')
print(citylist)

cityOfBirth = citylist.pop(4)
print(cityOfBirth)

del citylist[0]
#reverse
print(citylist)
citylist.reverse()
print(citylist)
citylist.reverse()
print(citylist)

citylist.sort()
print(citylist)
citylist.append('Vladimir')
citylist.append('Penza')
citylist.append('Vladivostok')
citylist.append('Nakhodka')
citylist.append('Murmansk')
citylist.append('Arkhangelsk')
print(citylist)
print(sorted(citylist))
length = len(citylist)
print(f"citylist has {length} elements")

##remove by value
citylist.remove('Penza') 
print(citylist)
#last element
print(citylist[-1])


