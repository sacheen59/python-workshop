# division 
try:
    first_number = int(input("Enter your first number: "))
    second_number = int(input("Enter your second number: "))
except ValueError:
    print("The number must be integer")
else:
    add = first_number + second_number
    print(add)
finally:
    print("done")

# try:
#     division = first_number/ second_number
#     print(division)
# except:
#     print("Denominator must not be zero")



# try:
#     print(x)
# except NameError:
#     print("x is not defined")

