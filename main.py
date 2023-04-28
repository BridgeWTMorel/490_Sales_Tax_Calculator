# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from dataclasses import dataclass


@dataclass
class ItemStock:
    name: str
    price: float
    type: str


def total_cost_including_tax(state, shopping_cart):
    if not isinstance(state, str) or not isinstance(shopping_cart, list):
        raise TypeError('Incorrect parameter types.')
    if len(shopping_cart) <= 0:
        raise IndexError('Shopping cart is empty.')

    total_cost = 0.00
    sales_tax = 0.00
    if state == 'NJ': sales_tax = 0.066
    elif state == 'PA': sales_tax = 0.06
    elif state != 'DE': raise ValueError('Incorrect state field.')

    for item in shopping_cart:
        tax = sales_tax
        if type(item.name) is not str or type(item.price) is not float or type(item.type) is not str:
            raise TypeError('Invalid item data fields.')
        if item.price <= 0.00: raise ValueError('Invalid item price.')

        if item.type == 'WIC Eligible Food': tax = 0.00
        elif item.type == 'Clothing':
            if state == 'PA': tax = 0.00
            elif 'fur' not in item.name and state == 'NJ': tax = 0.00
        elif item.type != 'everything else': raise ValueError('Invalid item category.')

        item_cost = item.price + item.price * tax
        total_cost = total_cost + item_cost
    return total_cost
