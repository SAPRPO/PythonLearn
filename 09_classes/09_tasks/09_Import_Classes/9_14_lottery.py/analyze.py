from lottery import list, ticket_combination

print(list)
winner_ticket = ticket_combination()
#print(winner_ticket)
#compare every symbol?
count = 1
while(True):
    play_result = ticket_combination()
    if(play_result != winner_ticket):
        print(f"Attempt: {count}, result: {play_result}")
        count = count+1
    else:
        print(f"Finish! Winner ticket: {winner_ticket}, Count = {count}")
        break