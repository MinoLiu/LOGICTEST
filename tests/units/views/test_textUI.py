def test_display_menu(test_textUI, mocker, capfd):
    # Mock input function first key 5, second key 4
    mock_input = mocker.patch('builtins.input', side_effect=["5", "4"])
    # Spy mock process_command
    mock_process_command = mocker.spy(test_textUI, 'process_command')
    test_textUI.display_menu()

    assert "Command must be integer, and in range 1 ~ 4" in str(capfd.readouterr())
    assert mock_process_command.call_count == 1
    assert mock_input.call_count == 2


def test_process_command_1(test_textUI, mocker, capfd):
    mocker.patch('builtins.input', return_value="1")
    mock_simulator = mocker.patch.object(test_textUI, '_TextUI__simulator')
    mock_simulator.load = mocker.MagicMock()

    test_textUI.process_command(1)
    assert mock_simulator.load.call_count == 1

    def mock_excpetion(value=None):
        raise Exception("test exception")

    mock_simulator.load = mock_excpetion
    test_textUI.process_command(1)
    assert "test exception" in str(capfd.readouterr())


def test_process_command_2(test_textUI, mocker, capfd):
    mocker.patch('builtins.input', side_effect=["-1", "0", "1"])
    mock_simulator = mocker.patch.object(test_textUI, '_TextUI__simulator')
    mock_simulator.has_input = False
    mock_simulator.input_length = 2
    mock_simulator.get_simulation_result = mocker.MagicMock(return_value="success")

    test_textUI.process_command(2)
    assert "Please load an lcf file" in str(capfd.readouterr())

    mock_simulator.has_input = True

    test_textUI.process_command(2)
    assert mock_simulator.get_simulation_result.call_count == 1
    assert "The value of input pin must be 0/1" in str(capfd.readouterr())

    def mock_excpetion(value=None):
        raise Exception("test exception")

    mock_simulator.get_simulation_result = mock_excpetion
    mocker.patch('builtins.input', side_effect=["0", "1"])
    test_textUI.process_command(2)
    assert "test exception" in str(capfd.readouterr())


def test_process_command_4(test_textUI, mocker, capfd):
    mock_simulator = mocker.patch.object(test_textUI, '_TextUI__simulator')
    mock_simulator.has_input = False
    mock_simulator.get_truth_table = mocker.MagicMock(return_value="success")

    test_textUI.process_command(3)
    assert "Please load an lcf file" in str(capfd.readouterr())

    mock_simulator.has_input = True

    test_textUI.process_command(3)
    assert "success" in str(capfd.readouterr())

    def mock_excpetion(value=None):
        raise Exception("test exception")

    mock_simulator.get_truth_table = mock_excpetion
    test_textUI.process_command(3)
    assert "test exception" in str(capfd.readouterr())
