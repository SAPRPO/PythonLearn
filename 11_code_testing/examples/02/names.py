from name_function_updated import get_formatted_name

print("Enter 'q' at any time to quit")
while(True):
    first = input("\nGive first name: ")
    if first == 'q':
        break
    last = input("Give last name: ")
    if last == 'q':
        break

    formatted_name = get_formatted_name(first, last)
    print(f"\tNealthy formatted name: {formatted_name}")