class Car():
    def __init__(self, brand, color, mileage):
        self.brand = brand
        self.color = color
        self.mileage = mileage

    def get_brand(self):
        print(self.brand)
    
    def get_mileage(self):
        return self.mileage

    def set_brand(self, new_brand):
        self.brand = new_brand

    def set_color(self, new_color):
        self.color = new_color

    def set_milage(self, new_mileage):
        self.milage = new_mileage

# ----------Huvudprogram----------
# Nu när klassen finns kan vi skapa objekt (variabler) med denna typ.
# Dessa objekt har också tillgång till klassens metoder (funktioner).
a_car = Car('Volvo', 'Blå', 1587)
a_car.get_brand()
a_car.set_brand('Renault')
a_car.get_brand()

b_car = Car("Royce", "white", 1200)
b_car.get_brand()