class Person:
    def __init__(self, full_name, age):
        self.full_name = full_name
        self.age = age

    @property
    def full_name(self):
        return self._full_name

    @full_name.setter
    def full_name(self, value):
        self._full_name = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        self._age = value


class Driver(Person):
    def __init__(self, full_name, age, driving_experience):
        super().__init__(full_name, age)
        self.driving_experience = driving_experience


class Engine:
    def __init__(self, power, manufacturer):
        self.power = power
        self.manufacturer = manufacturer


class Car:
    def __init__(self, brand, car_class, weight, car_driver, car_engine):
        self.brand = brand
        self.car_class = car_class
        self.weight = weight
        self.driver = car_driver
        self.engine = car_engine

    def start(self):
        print("Поехали")

    def stop(self):
        print("Останавливаемся")

    def turn_right(self):
        print("Поворот направо")

    def turn_left(self):
        print("Поворот налево")

    def to_string(self):
        return f"Brand: {self.brand}, Class: {self.car_class}, Weight: {self.weight}, " \
               f"Driver: {self.driver.full_name}, Age: {self.driver.age} " \
               f"Driving experience: {self.driver.driving_experience}, " \
               f"Motor: {self.engine.manufacturer}, Power: {self.engine.power}"


class Lorry(Car):
    def __init__(self, brand, car_class, weight, car_driver, car_engine, carrying_capacity):
        super().__init__(brand, car_class, weight, car_driver, car_engine)
        self.carrying_capacity = carrying_capacity

    def to_string(self):
        return super().to_string() + f", Carrying capacity: {self.carrying_capacity}"


class SportCar(Car):
    def __init__(self, brand, car_class, weight, car_driver, car_engine, top_speed):
        super().__init__(brand, car_class, weight, car_driver, car_engine)
        self.top_speed = top_speed

    def to_string(self):
        return super().to_string() + f", Top speed: {self.top_speed}"


driver = Driver("Kairat Nurtas", 35, 10)
engine = Engine(200, "Toyota")
car = Car("Toyota", "Sedan", 1500, driver, engine)

car.start()
car.turn_right()
car.stop()
print(car.to_string())

lorry = Lorry("Ford", "Lorry", 2500, driver, engine, 6000)
print(lorry.to_string())

sport_car = SportCar("Ferrari", "Sport", 1000, driver, engine, 290)
print(sport_car.to_string())
