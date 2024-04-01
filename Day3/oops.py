# class Animal:
#     name = "Cat"

#     def move(self):
#         print("This animal walk")


# animal = Animal()

# print(animal.name)
# animal.move()


# class Info:
    
#     def information(self,name,interest):
#         self.name = name
#         self.interest= interest
#         print(f"{self.name} is interested in {self.interest}")


# bahas = Info()
# bahas.information("Bahas","Django")


class Python:

    def __init__(self):
        print("This is the constructor which runs after creating the object")

    def display(self):
        print("This is the display method which runs after calling")


py = Python()

py.display()
p= Python()