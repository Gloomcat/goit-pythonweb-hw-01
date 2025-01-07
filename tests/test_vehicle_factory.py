import logging
import pytest
from goit_pythonweb_hw_01.vehicle_factory import USVehicleFactory, EUVehicleFactory, Vehicle

def test_us_vehicle_factory(caplog):
    caplog.set_level(logging.INFO)
    us_factory = USVehicleFactory()

    car = us_factory.create_car("Ford", "Mustang")
    car.start_engine()
    assert "Ford Mustang US Spec: Engine started" in caplog.text

    motorcycle = us_factory.create_motorcycle("Harley-Davidson", "Sportster")
    motorcycle.start_engine()
    assert "Harley-Davidson Sportster US Spec: Motor started" in caplog.text

def test_eu_vehicle_factory(caplog):
    caplog.set_level(logging.INFO)
    eu_factory = EUVehicleFactory()

    car = eu_factory.create_car("BMW", "3 Series")
    car.start_engine()
    assert "BMW 3 Series EU Spec: Engine started" in caplog.text

    motorcycle = eu_factory.create_motorcycle("Ducati", "Monster")
    motorcycle.start_engine()
    assert "Ducati Monster EU Spec: Motor started" in caplog.text
