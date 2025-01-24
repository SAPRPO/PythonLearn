dimensions = (200, 50)

print(dimensions[0])
print(dimensions[1])

#one element in tuple
#t = (3,)
#print(t)

for dimention in dimensions:
    print(dimention)
# Замена, переопределение кортежа

dimensions = (200, 50)
print("\nOriginal dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)
