
import pytest
from shopping_basket.inventory import *

def test_buy_and_sell_nikes_adidas():

    # Create inventory object
    inventory = Inventory()
    assert inventory.limit == 100
    assert inventory.total_items == 0

    # Add the new nike sneakers
    inventory.add_new_stock('Nike Sneakers', 50.00, 10)
    assert inventory.total_items == 10

    # Add the new Adidas sweatpants
    inventory.add_new_stock('Adidas sweatpants', 70.00, 5)
    assert inventory.total_items == 15

    inventory.remove_stock('Nike sneakers', 2)
    assert inventory.total == 13

    inventory.remove_stock('Adidas sweatpants', 1)
    assert inventory.total == 12



def test_default_inventory():
    """Test that the default limit is 100"""
    inventory = Inventory()
    assert inventory.limit == 100
    assert inventory.total_items == 0

def test_custom_inventory_limit():
    """Test that we can set a custom limit """
    inventory = Inventory(limit=25)
    assert inventory.limit == 25
    assert inventory.total_items == 0


# Fixture for repeating instantiating Inventory objects
@pytest.fixture
def no_stock_inventory():
    """Returns an empty inventory that can store 10 items"""
    return Inventory(10)

def test_add_new_stock_success(no_stock_inventory):
    no_stock_inventory.add_new_stock('Test Jacket', 10.00, 5)
    assert no_stock_inventory.total_items == 5
    assert no_stock_inventory.stocks['Test Jacket']['price'] == 10.00
    assert no_stock_inventory.stocks['Test Jacket']['quantity'] == 5

# Parametrizing Tests
# Either use Try/except to catch exceptions, but repetitous
# Parametrized functions allow you to test multiple scenarious using one function

@pytest.mark.parametrize('name,price,quantity,exception', [
    ('Test Jacket', 10.00, 0, InvalidQuantityException(
        'Cannot add a quantity of 0. All new stocks must have at least 1 item')),
    ('Test Jacket', 10.00, 25, NoSpaceException(
        'Cannot add these 25 items. Only 10 more items can be stored'))
    
])
def test_add_new_stock_bad_input(no_stock_inventory, name, price, quantity, exception):
    try:
        no_stock_inventory.add_new_stock(name, price, quantity)
    except (InvalidQuantityException, NoSpaceException) as inst:
        # First ensure the exception is of the right type
        assert isinstance(inst, type(exception))
        # Ensure that exceptions have the same message
        assert inst.args == exception.args
    else:
        pytest.fail("Expected error but found none")

"""
def test_add_new_stock_bad_input(name, price, quantity, exception):
    inventory = Inventory(10)
    try:
        inventory.add_new_stock(name, price, quantity)
    except (InvalidQuantityException, NoSpaceException) as inst:
        # First ensure the exception is of the right type
        assert isinstance(inst, type(exception))
        # Ensure that exceptions have the same message
        assert inst.args == exception.args
    else:
        pytest.fail("Expected error but found none")
"""



# New function that takes place of test_add_new_stock_bad_input 
# and test_add_new_stock_success


@pytest.mark.parametrize('name,price,quantity,exception', [
    ('Test Jacket', 10.00, 0, InvalidQuantityException(
        'Cannot add a quantity of 0. All new stocks must have at least 1 item')),
    ('Test Jacket', 10.00, 25, NoSpaceException(
        'Cannot add these 25 items. Only 10 more items can be stored')),
    ('Test Jacket', 10.00, 5, None)
    
])
def test_add_new_stock(no_stock_inventory, name, price, quantity, exception):
    try:
        no_stock_inventory.add_new_stock(name, price, quantity)
    except (InvalidQuantityException, NoSpaceException) as inst:
        # First ensure the exception is of the right type
        assert isinstance(inst, type(exception))
        # Ensure that exceptions have the same message
        assert inst.args == exception.args
    else:
        assert no_stock_inventory.total_items == quantity
        assert no_stock_inventory.stocks[name]['price'] == price
        assert no_stock_inventory.stocks[name]['quantity'] == quantity

