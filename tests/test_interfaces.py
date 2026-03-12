import builtins
from unittest.mock import patch, MagicMock

# Import the interface after mocking cli and cli2
import interface



# Test: _ask_mode() — valid inputs
def test_ask_mode_valid():
    with patch("builtins.input", side_effect=["1"]):
        assert interface._ask_mode() == 1

    with patch("builtins.input", side_effect=["2"]):
        assert interface._ask_mode() == 2


# Test: _ask_mode() — invalid then valid
def test_ask_mode_invalid_then_valid():
    with patch("builtins.input", side_effect=["abc", "5", "2"]):
        # Should ignore invalid input and accept the "2"
        assert interface._ask_mode() == 2



# Test: _ask_play_again() — valid
def test_ask_play_again_valid():
    with patch("builtins.input", side_effect=["y"]):
        assert interface._ask_play_again() is True

    with patch("builtins.input", side_effect=["n"]):
        assert interface._ask_play_again() is False


# Test: _ask_play_again() — invalid then valid
def test_ask_play_again_invalid_then_valid():
    with patch("builtins.input", side_effect=["maybe", "yes", "y"]):
        assert interface._ask_play_again() is True


# Test: main() launches Mode 1 correctly (mock cli.main)
def test_main_runs_mode1():
    # Mock the mode 1 and mode 2 main functions
    with patch("interface.mode1_main") as mode1_mock, 
         patch("interface.mode2_main") as mode2_mock, 
         patch("builtins.input", side_effect=["1", "n"]):

        interface.main()

        mode1_mock.assert_called_once()
        mode2_mock.assert_not_called()


# Test: main() launches Mode 2 correctly (mock cli2.main)
def test_main_runs_mode2():
    with patch("interface.mode1_main") as mode1_mock,
         patch("interface.mode2_main") as mode2_mock,
         patch("builtins.input", side_effect=["2", "n"]):

        interface.main()

        mode2_mock.assert_called_once()
        mode1_mock.assert_not_called()
