#age =16

while True:  #unlimited
    age = int(input("Enter your age: "))

    if age >=18:
        print("You are old enough to vote!")
        print("Have you registered to vote yet?")
    else:
        print("You are too young to vote.")
        print("Please register to vote as soon as you turn 18!")