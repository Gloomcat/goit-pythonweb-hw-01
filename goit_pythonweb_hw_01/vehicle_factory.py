import logging
from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, make: str, model: str, region: str) -> None:
        self.make: str = make
        self.model: str = model
        self.region: str = region

    @abstractmethod
    def start_engine(self) -> None:
        pass


class Car(Vehicle):
    def start_engine(self) -> None:
        logging.info(f"{self.make} {self.model} {self.region}: Engine started")


class Motorcycle(Vehicle):
    def start_engine(self) -> None:
        logging.info(f"{self.make} {self.model} {self.region}: Motor started")


class VehicleFactory(ABC):
    @abstractmethod
    def create_car(self, make: str, model: str) -> Vehicle:
        pass

    @abstractmethod
    def create_motorcycle(self, make: str, model: str) -> Vehicle:
        pass


class USVehicleFactory(VehicleFactory):
    def __init__(self) -> None:
        self.region: str = "US Spec"

    def create_car(self, make: str, model: str) -> Car:
        return Car(make, model, self.region)

    def create_motorcycle(self, make: str, model: str) -> Motorcycle:
        return Motorcycle(make, model, self.region)


class EUVehicleFactory(VehicleFactory):
    def __init__(self) -> None:
        self.region: str = "EU Spec"

    def create_car(self, make: str, model: str) -> Car:
        return Car(make, model, self.region)

    def create_motorcycle(self, make: str, model: str) -> Motorcycle:
        return Motorcycle(make, model, self.region)
