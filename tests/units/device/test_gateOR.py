import pytest


def test_init(test_gateOR):
    assert test_gateOR.name == 'gateOR'


def test_get_output_exception(test_gateOR):
    with pytest.raises(Exception) as execinfo:
        test_gateOR.get_output()
    assert test_gateOR.name in str(execinfo.value)


def test_add_input_pin(test_gateOR, test_new_iPin_1, test_new_iPin_2):
    test_gateOR.add_input_pin(test_new_iPin_1)
    assert test_gateOR._iPins[0] == test_new_iPin_1
    test_gateOR.add_input_pin(test_new_iPin_2)
    assert test_gateOR._iPins[1] == test_new_iPin_2


def test_get_output(test_gateOR):
    test_gateOR._iPins[0].set_input(True)
    test_gateOR._iPins[1].set_input(False)
    assert test_gateOR.get_output() is True

    test_gateOR._iPins[0].set_input(False)
    assert test_gateOR.get_output() is False
