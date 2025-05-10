import random
while(True):
    input_d = int(input("Enter digit (1-10):\n")) #Exception
#print(input_d)
    rd = random.randint(1, 10)
#print(rd)

    if input_d == rd:
        print(f"You write: {input_d}, is the same as from computer {rd} Ok!")
    else:
        print(f"You write: {input_d}, from computer {rd}. Error!")
