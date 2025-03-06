prompt = "print 'quit' for interrupt program: " 
message = ""
active = True
while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print(message)