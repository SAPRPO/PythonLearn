sandwich_orders = ['cheesburger', 'hamburger', 'bigMac', 'McChicken', 'McPizza']
finished_sandwiches = []

while sandwich_orders:
    temp_sandwich = sandwich_orders.pop()
    print(f"I made your {temp_sandwich} sandwich")
    finished_sandwiches.append(temp_sandwich)

print("These sandwiches are done:")
count =1 
for sandwich in finished_sandwiches:
    print(f'{count}. {sandwich.title()}')
    count += 1