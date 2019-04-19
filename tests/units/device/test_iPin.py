import pytest


def test_init(test_iPin):
    assert test_iPin.name == 'iPin'


def test_add_input_pin(test_iPin):
    with pytest.raises(Exception) as execinfo:
        test_iPin.add_input_pin(test_iPin)

    assert "Please use set_input" in str(execinfo.value)


def test_get_output_exception(test_iPin):
    with pytest.raises(Exception) as execinfo:
        test_iPin.get_output()
    assert test_iPin.name in str(execinfo.value)


def test_set_input(test_iPin):
    test_iPin.set_input(True)
    assert test_iPin.has_input is True
    assert test_iPin.get_output() is True
