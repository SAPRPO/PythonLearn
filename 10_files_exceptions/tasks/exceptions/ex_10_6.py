print("enter two numbers:")

try:
    first_number = int(input("Enter first number: "))
    second_number = int(input("Enter second number: "))
except ValueError:
    print("Enter a number, not a symbol!")
else:
    print(f"Result of addition: {first_number+second_number}")
