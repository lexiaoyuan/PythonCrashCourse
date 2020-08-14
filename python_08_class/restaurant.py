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


restaurant = Restaurant('传统客栈', '综合')
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)
restaurant.describe_restaurant()
restaurant.open_restaurant()

restaurant2 = Restaurant('海底捞', '火锅')
restaurant2.describe_restaurant()

restaurant3 = Restaurant('自助餐', '自助')
restaurant3.describe_restaurant()

restaurant4 = Restaurant('蔡林记', '热干面')
restaurant4.describe_restaurant()
restaurant4.number_served = 100
restaurant4.describe_restaurant()

restaurant4.set_number_served(150)
restaurant4.describe_restaurant()

restaurant4.increment_number_served(50)
restaurant4.describe_restaurant()
