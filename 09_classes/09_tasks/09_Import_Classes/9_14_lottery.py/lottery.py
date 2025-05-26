from random import choice

list = [ 0, 1, 2, 3, 4, 5,6, 7,8,9 ,'z','a','b','c','d']

def ticket_combination():
    res_string=""
    for r in range(0,4):
        result = choice(list)
        #int or not?
        if isinstance(result, int):  
            res_string += str(result)
        else:
            res_string += result.capitalize()
    return res_string



def print_winner_ticket(res_string):
    print(f"Your ticket {res_string} is a winning ticket!")

res_string = ticket_combination()
print_winner_ticket(res_string)