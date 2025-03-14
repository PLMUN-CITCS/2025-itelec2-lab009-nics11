user_input = input("Enter a number: ")

try:
    number = int(user_input)
    
    if number % 2 == 0:
        print("The number", number, "is Even.")
    else:
        print("The number", number, "is Odd.")
except ValueError:
    print("Invalid input. Please enter an integer.")