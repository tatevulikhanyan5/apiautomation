import pytest

from repodemo.restfull_booker.api.endpoints import Endpoints
from repodemo.restfull_booker.api.payloads import JsonBuilders

driver = None

@pytest.fixture
def get_driver(request):
    # Add in here each page from the POM in order to initialize the driver for each one.
    request.cls.endpoints = Endpoints()
    request.cls.jsons = JsonBuilders()

    yield
    print("pass")


