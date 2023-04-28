from main import *


def test_happy_path_total_cost_including_tax():
    shopping_cart = []
    cart.append(ItemStock('shirt', 10.00, 'Clothing'))
    cart.append(ItemStock('fur jacket', 15.00, 'Clothing'))
    cart.append(ItemStock('beans', 20.00, 'WIC Eligible Food'))
    cart.append(ItemStock('stapler', 25.00, 'everything else'))

    assert total_cost_including_tax('DE', shopping_cart) == 70.0
    assert total_cost_including_tax('PA', shopping_cart) == 73.0
    assert total_cost_including_tax('NJ', shopping_cart) == 72.64
