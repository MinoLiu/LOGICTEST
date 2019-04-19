import pytest
from modules.device.base import Device
from modules.device import DeviceFactory


@pytest.fixture(scope="session")
def test_device():
    return Device()


@pytest.fixture(scope="session")
def test_factory():
    return DeviceFactory()


@pytest.fixture(scope="session")
def test_oPin(test_factory):
    return test_factory.create_oPin()


@pytest.fixture(scope="function")
def test_new_iPin_1(test_factory):
    return test_factory.create_iPin()


@pytest.fixture(scope="function")
def test_new_iPin_2(test_factory):
    return test_factory.create_iPin()


@pytest.fixture(scope="session")
def test_iPin(test_factory):
    return test_factory.create_iPin()


@pytest.fixture(scope="session")
def test_gateAND(test_factory):
    return test_factory.create_gate(1)


@pytest.fixture(scope="session")
def test_gateOR(test_factory):
    return test_factory.create_gate(2)


@pytest.fixture(scope="session")
def test_gateNOT(test_factory):
    return test_factory.create_gate(3)
