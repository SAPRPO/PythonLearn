#slices 
players = ['charles', 'martina', 'ivan', 'mike', 'alex']

print(players[0:3]) # print part of list 0-2
print(players[1:4]) #1-3
print(players[:4]) # begin from 0
print(players[2:]) #begin from 3
print(players[-3:]) # last 3

for player in  players[:3]:
    print(player.title())