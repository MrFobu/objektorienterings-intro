class Car():
    def __init__(self, brand, color, mileage):
        self.brand = brand
        self.color = color
        self.mileage = mileage

    def get_brand(self):
        print(self.brand)
    
    def get_mileage(self):
        return self.mileage
    
    def get_color(self):
        return self.color

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
b_car.set_color("Grey")
b_car.get_brand()
b_car.get_color()

c_car = Car("Clowncar","Red","2405")

d_car = Car("Lampadati", "yellow",1300)

my_cars = [a_car, b_car, c_car, d_car]


def list_cars(my_cars):
    while True:
        print(f"\nCar menu\nList brands [b] \nList colors [c]\nList milage [m]\nquit [q]")
        menu = input("Select menu option :")
        if menu == "b":
            print("\nBrands:\n")
            for obj in my_cars:
                print(obj.brand)
            input("press enter to continue ")
        elif menu == "c":
            print("\nColors:\n")
            for obj in my_cars:
                print(obj.color)
            input("press enter to continue ")
        elif menu == "m":
            print("\nMileage:\n")
            for obj in my_cars:
                print(obj.mileage)
            input("press enter to continue ")
        elif menu == "q":
            break
        else:
            print("\ninvalid input")
    
    


list_cars(my_cars)