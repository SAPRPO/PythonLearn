current_users = ['Alex', 'JayZ', 'Nelly', 'admin', 'Max', 'Den', 'Dmitry']
new_users = ['Nelly','ALEX', 'admin', 'Pinguin', 'Vladimir']
nu_copy = []
for new_user in new_users:
    if new_user == 'admin':
        nu_copy.append(new_user)
    else:
        nu_copy.append(new_user.title())
    #print(new_user.title())

print(nu_copy)
for new_user in nu_copy:
    if new_user in current_users:
        print(f"{new_user}, you need to use new username")
    else:
        print(f"{new_user}, your username is available")