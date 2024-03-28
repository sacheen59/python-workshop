# collection of data in key value pair

information = {
    "name": "sachin",
    "faculty": "DIT",
    "semester": 3
}

# to find the length of information

print(len(information))


# accessing the element

print(information["name"])

# updating the element

information["name"] = "Saksham"
print(information)

# adding item to the dictionary

information.update({"address":"Bharatpur"})
print(information)

# removing the item
information.pop("name")
print(information)

# looping through items in dictionary

for k in information.keys():
    print(k)

for v in information.values():
    print(v)

for key,value in information.items():
    print(f"{key} => {value}")
