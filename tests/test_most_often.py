from lib.most_often import MostOften
import pytest

#Testing for adding items to the list
def test_add_new_item():
    itemlist = MostOften([1, 2, 3, 4, 5])
    itemlist.add_new(6)
    assert itemlist.starting_list == [1, 2, 3, 4, 5, 6]

#Testing for the most often item
def test_most_often_item():
    itemlist = MostOften([1, 2, 2, 2, 3, 4, 4, 5, 5, 6])
    result = itemlist.get_most_often()
    assert result == 2
#Testing for duplicate most items
def test_two_most_often_items():
    itemlist = MostOften([1, 2, 2, 2, 3, 4, 4, 4, 5, 5, 6])
    result = itemlist.get_most_often()
    assert result == 'no clear winner'

#Error testing
def test_list_is_not_list():
    with pytest.raises(Exception) as e:
        itemlist = MostOften('test')
    error = str(e.value)
    assert error == 'Incorrect input type'

def test_item_cant_be_added():
    itemlist = MostOften([1, 2, 3, 4, 5])
    with pytest.raises(Exception) as e:
        itemlist.add_new(None)
    assert str(e.value) == 'Item cannot be added'

