class Car:
    def __init__(self, name, model, year):
        self.name = name
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        print(f"{self.name} {self.model} {self.year}")

    def odometer(self, mile):
        self.odometer_reading = mile
        print(f"This car has {self.odometer_reading} in it")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print(f"{self.odometer_reading} can't be changed")

    def increment(self, n):
        self.odometer_reading += n

    def fueltank(self):
        print(f"This of fuel capacity")


class Battery:
    def __init__(self, battery_size=75):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"This car is of {self.battery_size} kWh battery size")

    def get_range(self):
        if self.battery_size == 75:
            range_Ecar = 260
        elif self.battery_size >= 100:
            range_Ecar = 300
        print(f"This car can go up to {range_Ecar} in one full charge")


class ElectricCar(Car):
    def __init__(self, name, model, year):
        super().__init__(name, model, year)
        self.battery = Battery()
        
    def fueltank(self):
        print("Electric car don't have fuel tank")


my_tesla = ElectricCar('Tesla', 'R8', 2019)
my_tesla.get_descriptive_name()
my_tesla.fueltank()
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

"""
output
Tesla R8 2019
Electric car don't have fuel tank
This car is of 75 kWh battery size
This car can go up to 260 in one full charge

"""
