class Restaurant:
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type
        self.timing = '10:00 AM to 4:00 PM'

    def describe_restaurant(self):
        print(f'{self.name} Hotel is {self.cuisine_type}')
        print(f"The hotel will be open at {self.timing}")

    def open_restaurant(self):
        print(f"Hey {self.name} is still open")


my_hotel = Restaurant("Gopi Foods", "south indian")
my_hotel.timing = '10:00 - 23:00'
my_hotel.describe_restaurant()
my_hotel.open_restaurant()
Bmt_hotel = Restaurant("Ones More", "Mahrastrian")
Bmt_hotel.describe_restaurant()
Bmt_hotel.open_restaurant()
print()
Restaurant.describe_restaurant(my_hotel)

"""
output

Gopi Foods Hotel is south indian
The hotel will be open at 10:00 - 23:00
Hey Gopi Foods is still open
Ones More Hotel is Mahrastrian
The hotel will be open at 10:00 AM to 4:00 PM
Hey Ones More is still open

Gopi Foods Hotel is south indian
The hotel will be open at 10:00 - 23:00

"""
