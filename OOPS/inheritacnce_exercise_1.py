"Created a Icreamstand childclass from Restaurant Parent class"

class Restaurant:
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type
        self.timing = '10:00 AM to 4:00 PM'

    def describe_restaurant(self):
        print(f'{self.name} is a {self.cuisine_type}')
        print(f"The restaurant will be open from {self.timing}")

    def check_restaurant(self):
        print(f"Hey {self.name} {self.cuisine_type} is still open")


class IceCreamStand(Restaurant):
    def __init__(self, name, cuisine_type):
        super().__init__(name, cuisine_type)
        self.flavours = ["Strawberry", "Kazatta", "Vennila"]

    def get_flavours(self):
        print("The available flavours are")
        for x in self.flavours:
            print(f"\t{x}")


my_icecream_shop = IceCreamStand("Arun", "Icream_shop")
my_icecream_shop.describe_restaurant()
my_icecream_shop.check_restaurant()
my_icecream_shop.get_flavours()

"""
Output
Arun is a Icream_shop
The restaurant will be open from 10:00 AM to 4:00 PM
Hey Arun Icream_shop is still open
The available flavours are
	Strawberry
	Kazatta
	Vennila
"""
