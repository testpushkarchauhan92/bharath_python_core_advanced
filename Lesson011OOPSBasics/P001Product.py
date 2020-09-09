class Product:

    # Parameterized Constructor
    def __init__(self):
        self.name = 'Samsung'
        self.description = 'Its Cool'
        self.price = 800

    # Instance method # self is similar to this
    def display(self):
        print(self.name)
        print(self.price)
        print(self.description)

p1 = Product()
p1.display()

p2 = Product()
p2.display()
