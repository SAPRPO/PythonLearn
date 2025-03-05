prompt ="how many places do you want to reserve? "
places=int(input(prompt))

if places > 8:
    print("you have to wait for a table")
else:
    print("your table is ready")