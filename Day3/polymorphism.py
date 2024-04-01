class Baba:
    def property(self):
        print("Baba ko property")

class Me(Baba):
    def property(self):
        print("Mero property")
        super().property()


# b = Baba()
# b.property()
# m = Me()
# m.property()
        
# for x in Baba(),Me():
#     x.property()
        
m = Me()
m.property()