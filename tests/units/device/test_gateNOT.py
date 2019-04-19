import pytest


def test_init(test_gateNOT):
    assert test_gateNOT.name == 'gateNOT'


def test_get_output_exception(test_gateNOT):
    with pytest.raises(Exception) as execinfo:
        test_gateNOT.get_output()
    assert test_gateNOT.name in str(execinfo.value)


def test_add_input_pin(test_gateNOT, test_new_iPin_1):
    test_gateNOT.add_input_pin(test_new_iPin_1)
    assert test_gateNOT._iPins[0] == test_new_iPin_1


def test_get_output(test_gateNOT):
    test_gateNOT._iPins[0].set_input(True)
    assert test_gateNOT.get_output() is False

    test_gateNOT._iPins[0].set_input(False)
    assert test_gateNOT.get_output() is True
