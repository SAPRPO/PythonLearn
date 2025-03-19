def greet_users(names):
    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)
    
names = ['mark', 'liza', 'nick']
greet_users(names)
