squares = []
for value in range(1,11):
    #square = value**2
    #print(square)
    squares.append(value**2)

print(squares)

digits = [1,2,3,4,5,6,7,8,9] 
min(digits) 
max(digits) 
sum(digits) 
print(f"min: {min(digits)}, max: {max(digits)}, sum: {sum(digits)}")

#list generator
squares = [value**2 for value in range(1,11)]
print(squares)