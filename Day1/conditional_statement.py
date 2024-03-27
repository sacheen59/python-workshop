"""
if(condition){
 statement
}
else if(condition){
statement
}
else{
statement
}
"""

"""
if condtion:
    statement
elif condition:
    statement
else:
    statement
"""

# day = int(input("Enter your day: "))

# if day == 14:
#     print("Aaja tw workshop maa jani ho")
# else:
#     print("xyaa aaja jana man thiyo raina raixa")

num1 = int(input("Enter your first number: "))
num2 = int(input("Enter your second number: "))
num3 = int(input("Enter your third number: "))

if num1 > num2 and num1 > num3:
    print("greater number is: ",num1)
elif num2 > num1 and num2 > num3:
    print("greater number is: ",num2)
else:
    print("greater number is: ",num3)


