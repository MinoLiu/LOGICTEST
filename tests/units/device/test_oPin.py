import pytest


def test_init(test_oPin):
    assert test_oPin.name == 'oPin'


def test_get_output_exception(test_oPin):
    with pytest.raises(Exception) as execinfo:
        test_oPin.get_output()
    assert test_oPin.name in str(execinfo.value)


def test_add_input_pin(test_oPin, test_iPin):
    test_oPin.add_input_pin(test_iPin)
    assert test_oPin._iPins[0] == test_iPin


def test_get_output(test_oPin):
    assert test_oPin.get_output() is True
