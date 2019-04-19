import os
import pytest
from modules.simulator import LogicSimulator


@pytest.yield_fixture()
def test_LS():
    with open("test.lcf", mode="w", encoding="UTF-8") as f:
        f.write("""3
3
1 -1 2.1 3.1 0
3 -2 0
2 2.1 -3 0""")
    yield LogicSimulator()
    os.remove("test.lcf")


@pytest.yield_fixture()
def test_error_LS():
    with open("test.lcf", mode="w", encoding="UTF-8") as f:
        f.write("""3
3
1 -12r1 s 0
3 -31243 0
2 s1 et 0""")
    yield LogicSimulator()
    os.remove("test.lcf")


@pytest.yield_fixture()
def test_exception_LS():
    with open("test.lcf", mode="w", encoding="UTF-8") as f:
        f.write("""2
2
1 -1 2.1 0
2 -2 1.1 0""")
    yield LogicSimulator()
    os.remove("test.lcf")
