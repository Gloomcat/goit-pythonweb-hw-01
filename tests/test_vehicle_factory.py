import logging
import pytest
from io import StringIO
from goit_pythonweb_hw_01.vehicle_factory import (
    USVehicleFactory,
    EUVehicleFactory,
    Vehicle,
)

@pytest.fixture
def caplog():
    stream = StringIO()
    handler = logging.StreamHandler(stream)
    logger = logging.getLogger("VehicleFactory")
    logger.addHandler(handler)
    yield stream
    logger.removeHandler(handler)


def test_us_vehicle_factory(caplog):
    us_factory = USVehicleFactory()

    car = us_factory.create_car("Ford", "Mustang")
    car.start_engine()
    assert (
        "Ford Mustang US Spec: Engine started"
        in caplog.getvalue()
    )

    motorcycle = us_factory.create_motorcycle("Harley-Davidson", "Sportster")
    motorcycle.start_engine()
    assert (
        "Harley-Davidson Sportster US Spec: Motor started"
        in caplog.getvalue()
    )

def test_eu_vehicle_factory(caplog):
    eu_factory = EUVehicleFactory()

    car = eu_factory.create_car("BMW", "3 Series")
    car.start_engine()
    assert (
        "BMW 3 Series EU Spec: Engine started"
        in caplog.getvalue()
    )

    motorcycle = eu_factory.create_motorcycle("Ducati", "Monster")
    motorcycle.start_engine()
    assert (
        "Ducati Monster EU Spec: Motor started"
        in caplog.getvalue()
    )
