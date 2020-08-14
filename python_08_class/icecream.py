class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print("The name of the restaurant is " + self.restaurant_name.title())
        print("The type of the restaurant is " + self.cuisine_type.title())
        print("The number of the restaurant is " + str(self.number_served))

    def open_restaurant(self):
        print("The " + self.restaurant_name.title() + "is open")

    def set_number_served(self, number_served):
        self.number_served = number_served

    def increment_number_served(self, number_served):
        self.number_served += number_served


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = []

    def show_icecreams(self):
        for i in self.flavors:
            print(i)


icecream = IceCreamStand('冰淇淋', '冷饮')
icecream.flavors = ['草莓', '西瓜', '芒果', '蜜桃']
icecream.show_icecreams()
