import pytest
from modules.view.TextUI import TextUI


@pytest.fixture()
def test_textUI():
    return TextUI()
