prompt = "print 'quit' for interrupt program: " 
message = ""
while message != 'quit':
    message = input(prompt)
    if message != 'quit':
        print(message)