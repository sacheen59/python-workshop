
# addtion function 
def add(x,y):
    return x + y

def sub(x,y):
    return x - y

def multiplication(x,y):
    return x * y

def division(x,y):
    return x/y

# input from the user 
first_number = float(input("Enter your first number: "))
second_number = float(input("Enter your second number: "))


# user choice for operation
choice = input('Enter + for addition, - for subtraction, * for multiplication and / for division: ')


if choice == '+':
    print("The addition is:", add(first_number, second_number))
elif choice == '-':
    print("The subtraction is:", sub(first_number,second_number))
elif choice == '*':
    print("The product is:",multiplication(first_number,second_number))
elif choice == '/':
    print("The division is:",division(first_number,second_number))
else:
    print("Invalid choice")

# print(add(first_number, second_number))
# print(sub(first_number,second_number))
# print(multiplication(first_number,second_number))
# print(division(first_number,second_number))