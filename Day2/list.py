# list is the collection of data in contiguous memory

# list_name = [1,"sachin"]


fruits = ["banana","apple","mango","pineapple","orange"]

print(fruits)

# to find the length of an array elements 
print(len(fruits))

# accessing the list element

print(fruits[0])
print(fruits[2])
print(fruits[-1])
print(fruits[1:])
print(fruits[:4])
print(fruits[0::2])

# for loop and membership operator(in, not in)
print("----------------")
for f in fruits:
    print(f)

# methods of list in python

# update

fruits[0] = "papaya"
print(fruits)

fruits.append("banana")
print(fruits)

fruits.insert(1,"Pumpkin")
print(fruits)


# extending one list element with another

positive_number = [1,2,3,4,5,6]
negative_number = [-1,-2,-3.-4,-5]
negative_number.extend(positive_number)
print(negative_number)


# removing the item

meat = ["chicken","mutton","buff","pork"]

meat.pop()
print(meat)


# facebook_username = ["bahas","sulav","saksham","sachin","Roshni"]

# delete = "delete"
# user = input("Enter your username: ")

# if user == "saksham" and delete == "delete":
#     facebook_username.remove('saksham')

# print(facebook_username)

post = ['dashain post','tihar post','teej post']
print(post)

# del post
# print(post)

# post.clear()
# print(post)







