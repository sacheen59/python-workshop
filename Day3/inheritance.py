# single inheritance
# class Animal:

#     def animal(self):
#         print("this is the method from animal class")


# class Cat(Animal):

#     def something(self):
#         print("This is the method from cat class")



# c = Cat()

# c.animal()
# c.something()

# multilevel inheritance
# class Hajurbaa:

#     def hajurbaakoproperty(self):
#         print("yo chai hajurbaa ko property")

# class Baba(Hajurbaa):
#     def babakoproperty(self):
#         print("yo chai baba ko property ")

# class Me(Baba):
#     def meroproperty(self):
#         print("yo chai mero property")


# me = Me()
# me.hajurbaakoproperty()
# me.babakoproperty()
# me.meroproperty()


# multiple inheritance
class Hajurbaa:

    def hajurbaakoproperty(self):
        print("yo chai hajurbaa ko property")

class Baba:
    def babakoproperty(self):
        print("yo chai baba ko property ")

class Me(Baba, Hajurbaa):
    def meroproperty(self):
        print("yo chai mero property")


me = Me()
me.hajurbaakoproperty()
me.babakoproperty()
me.meroproperty()