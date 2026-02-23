num = int(input("Enter a number: "))

if num < 0:
    print("Invalid input – negative numbers not allowed.")
elif num % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")