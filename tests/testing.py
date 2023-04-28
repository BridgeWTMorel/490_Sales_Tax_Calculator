from main import *
import pytest


def test_happy_path_total_cost_including_tax():
    shopping_cart = []
    shopping_cart.append(ItemStock('shirt', 10.00, 'Clothing'))
    shopping_cart.append(ItemStock('fur jacket', 15.00, 'Clothing'))
    shopping_cart.append(ItemStock('beans', 20.00, 'WIC Eligible Food'))
    shopping_cart.append(ItemStock('stapler', 25.00, 'everything else'))
    assert total_cost_including_tax('DE', shopping_cart) == 70.0
    assert total_cost_including_tax('PA', shopping_cart) == 71.5
    assert total_cost_including_tax('NJ', shopping_cart) == 72.64

    assert total_cost_including_tax('DE', [ItemStock('beans', 10.00, 'WIC Eligible Food')]) == 10.00
    assert total_cost_including_tax('PA', [ItemStock('beans', 10.00, 'WIC Eligible Food')]) == 10.00
    assert total_cost_including_tax('NJ', [ItemStock('beans', 10.00, 'WIC Eligible Food')]) == 10.00

    assert total_cost_including_tax('DE', [ItemStock('jeans', 10.00, 'Clothing')]) == 10.00
    assert total_cost_including_tax('PA', [ItemStock('jeans', 10.00, 'Clothing')]) == 10.00
    assert total_cost_including_tax('NJ', [ItemStock('jeans', 10.00, 'Clothing')]) == 10.00

    assert total_cost_including_tax('DE', [ItemStock('bucket', 10.00, 'everything else')]) == 10.00
    assert total_cost_including_tax('PA', [ItemStock('bucket', 10.00, 'everything else')]) == 10.6
    assert total_cost_including_tax('NJ', [ItemStock('bucket', 10.00, 'everything else')]) == 10.66


def test_bad_data_total_cost_including_tax():
    with pytest.raises(TypeError, match=r'Incorrect parameter types.'):
        total_cost_including_tax(500, 33)
    with pytest.raises(ValueError, match=r'Incorrect state field.'):
        total_cost_including_tax('NewYork', [ItemStock('stapler', 533.33, 'everything else')])
    with pytest.raises(ValueError, match=r'Invalid item price.'):
        total_cost_including_tax('DE', [ItemStock('Beans', -10.00, 'WIC Eligible Food')])
    with pytest.raises(ValueError, match=r'Invalid item category.'):
        total_cost_including_tax('PA', [ItemStock('Beans', 10.00, 'bad category')])

    with pytest.raises(TypeError, match=r'Invalid item data fields.'):
        total_cost_including_tax('DE', [ItemStock(99, 10.00, 'WIC Eligible Food')])
    with pytest.raises(TypeError, match=r'Invalid item data fields.'):
        total_cost_including_tax('PA', [ItemStock('shirt', '99', 'Clothing')])
    with pytest.raises(TypeError, match=r'Invalid item data fields.'):
        total_cost_including_tax('NJ', [ItemStock('fur jacket', 10.00, 99)])


def test_edge_cases_total_cost_including_tax():
    with pytest.raises(IndexError, match=r'Shopping cart is empty.'):
        total_cost_including_tax('DE', [])
    assert total_cost_including_tax('NJ', [ItemStock('fur-lined coat', 100.00, 'Clothing')]) == 106.6
    assert total_cost_including_tax('PA', [ItemStock('fur-lined coat', 100.00, 'Clothing')]) == 100.0
    assert total_cost_including_tax('DE', [ItemStock('fur-lined coat', 100.00, 'Clothing')]) == 100.0
    assert total_cost_including_tax('NJ', [ItemStock('rain coat', 100.00, 'Clothing')]) == 100.0
