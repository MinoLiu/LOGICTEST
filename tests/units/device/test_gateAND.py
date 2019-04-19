import pytest


def test_init(test_gateAND):
    assert test_gateAND.name == 'gateAND'


def test_get_output_exception(test_gateAND):
    with pytest.raises(Exception) as execinfo:
        test_gateAND.get_output()
    assert test_gateAND.name in str(execinfo.value)


def test_add_input_pin(test_gateAND, test_new_iPin_1, test_new_iPin_2):
    test_gateAND.add_input_pin(test_new_iPin_1)
    assert test_gateAND._iPins[0] == test_new_iPin_1
    test_gateAND.add_input_pin(test_new_iPin_2)
    assert test_gateAND._iPins[1] == test_new_iPin_2


def test_get_output(test_gateAND):
    test_gateAND._iPins[0].set_input(True)
    test_gateAND._iPins[1].set_input(False)
    assert test_gateAND.get_output() is False

    test_gateAND._iPins[1].set_input(True)
    assert test_gateAND.get_output() is True
