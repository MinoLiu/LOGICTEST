import pytest


def test_init(test_LS):
    assert test_LS.name == "Logic simulator"


def test_error_load(test_error_LS):
    with pytest.raises(ValueError) as execinfo:
        test_error_LS.load("./notfound.lcf")
    assert "make sure the file exists" in str(execinfo.value)

    with pytest.raises(Exception) as execinfo:
        test_error_LS.load("./test.lcf")

    assert "context not valid" in str(execinfo.value)


def test_get_truth_table(test_LS):
    test_LS.reset()
    with pytest.raises(Exception) as execinfo:
        test_LS.get_truth_table()

    assert test_LS.name in str(execinfo.value)

    test_LS.load("./test.lcf")
    assert test_LS.get_truth_table() == """Circuit Truth table:
i i i | o
1 2 3 | 0
---------
0 0 0 | 0
0 0 1 | 0
0 1 0 | 0
0 1 1 | 0
1 0 0 | 1
1 0 1 | 1
1 1 0 | 0
1 1 1 | 0
"""


def test_get_simulation_result(test_LS):
    test_LS.load("test.lcf")
    assert test_LS.get_simulation_result([True, False, True]) == "1 0 1 | 1\n"

    assert test_LS.get_simulation_result([True, True, False]) == "1 1 0 | 0\n"


def test_exception_get_simulation_result(test_exception_LS):
    test_exception_LS.load("test.lcf")
    with pytest.raises(Exception) as execinfo:
        test_exception_LS.get_simulation_result([True, False, True])

    assert "Input length not equal" in str(execinfo.value)

    with pytest.raises(Exception) as execinfo:
        test_exception_LS.get_simulation_result([True, False])

    assert "Simulator has no output" in str(execinfo.value)
