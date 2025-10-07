from lib.high_value import HighValue
import pytest

##Testing first function
def test_first_return_highest():
    value = HighValue(5, 2)
    result = value.get_highest()
    assert result == ('First value is higher')
def test_second_return_highest():
    value = HighValue(2, 2.1)
    result = value.get_highest()
    assert result == ('Second value is higher')
def test_values_equal():
    value = HighValue(6, 6)
    result = value.get_highest()
    assert result == 'Values are equal'

##Testing second function
def test_add_to_first_value():
    value = HighValue(2, 4)
    value.add(8, 'first')
    assert value.value_first == 10
def test_add_to_second_value():
    value = HighValue(2, 4)
    value.add(8, 'second')
    assert value.value_second == 12

def test_is_not_correct_selection():
    value = HighValue(2, 4)
    with pytest.raises(Exception) as e:
        value.add(8, 5)
    error = str(e.value)
    assert error == 'Incorrect selection'
