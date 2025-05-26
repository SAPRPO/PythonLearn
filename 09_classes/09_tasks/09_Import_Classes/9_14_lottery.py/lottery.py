from random import choice

list = [ 0, 1, 2, 3, 4, 5,6, 7,8,9 ,'z','a','b','c','d']
res_string=""
for r in range(0,4):
    result = choice(list)
    #int or not?
    if isinstance(result, int):  
        res_string += str(result)
    else:
        res_string += result.capitalize()

print(f"Your ticket {res_string} is a winning ticket!")