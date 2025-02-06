usernames = []
#usernames = ['Alex', 'JayZ', 'Nelly', 'admin', 'Max', 'Den', 'Dmitry']

if usernames:
    for username in usernames:
    #print(username)
        if username == 'admin':
            print(f"Hello {username}! Do you want to see report?")
        else:
            print(f"Hello {username}! Glad to see you")
else:
    print('Need to add users in our list')  
