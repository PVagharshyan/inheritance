class Transport:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def start(self):
        print(f"Start {self.__class__.__name__}")

    def stop(self):
        print(f"Stop {self.__class__.__name__}")

    def display_info(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")

class Car(Transport):
    def __init__(self, brand, model, year, count_doors):
        super().__init__(brand, model, year)
        self.count_doors = count_doors

    def start(self):
        print("The car's engine is starting.")

    def display_info(self):
        super().display_info()
        print(f"Number of Doors: {self.count_doors}")


class Motorcycle(Transport):
    def __init__(self, brand, model, year, count_wheels):
        super().__init__(brand, model, year)
        self.count_wheels = count_wheels

    def start(self):
        print("The motorcycle's engine is starting.")

    def display_info(self):
        super().display_info()
        print(f"Number of Wheels: {self.count_wheels}")


class Bicycle(Transport):
    def __init__(self, brand, model, year, material):
        super().__init__(brand, model, year)
        self.material = material

    def start(self):
        print("Pedaling the bicycle to start moving.")

    def display_info(self):
        super().display_info()
        print(f"Frame Material: {self.material}")

car = Car("Ford", "Mustang", 2022, 2)
motorcycle = Motorcycle("Harley-Davidson", "Sportster", 2021, 2)
bicycle = Bicycle("Giant", "Defy", 2020, "Carbon Fiber")

car.start()  
motorcycle.start()
bicycle.start()  

car.display_info()

motorcycle.display_info()

bicycle.display_info()
