from abc import ABC, abstractmethod

# Abstract base class for all vehicles
class Vehicle(ABC):
    def __init__(self, make: str, model: str):
        self.make = make
        self.model = model

    @abstractmethod
    def start_engine(self):
        pass

# Concrete class for Car
class Car(Vehicle):
    def start_engine(self):
        print(f"{self.make} {self.model}: Engine started")

# Concrete class for Motorcycle
class Motorcycle(Vehicle):
    def start_engine(self):
        print(f"{self.make} {self.model}: Engine started")
