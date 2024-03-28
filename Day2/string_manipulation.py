# workshop = "we are here in the python workshop"

# to find the length of character

# print(len(workshop))

#accessing the character from string

# print(workshop[0])
# print(workshop[0:10])
# print(workshop[1:])
# print(workshop[:5])
# print(workshop[0:20:2])
# print(workshop[-1])

# methods of string

# to convert string in uppercase
text = "we are learning python"
print(text.upper())

# to convert string into lower case
upper_text = "WE ARE LEARNING STRING MANIPULATION"
print(upper_text.lower())

# to remove the whitespace from the start and end of the string
greet = " hello world  "
print(greet)
print(greet.strip())

# to replace character
thankyou = "Thank you Bahas to participate in python workshop"

print(thankyou.replace("python","React"))

# split method in python
text = "Hello ! world"
wordlist = text.split('!')
print(wordlist)


# formatted string 

a = 10
b = 20
c = 30
# print("The value of a and b is:",a,b)

print(f"The value of a is {a} and b is {b} and c is {c}")

