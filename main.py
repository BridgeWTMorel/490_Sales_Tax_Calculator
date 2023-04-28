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
    if isinstance(state, str) and isinstance(shopping_cart, ItemStock):
        raise TypeError('Incorrect parameter Types.')
    if len(shopping_cart) <= 0:
        raise IndexError('Shopping cart is empty.')

    total_cost = 0.00
    sales_tax = 0.00
    if state == 'NJ': sales_tax = 0.066
    elif state == 'PA': sales_tax = 0.06
    elif state != 'DE': raise ValueError('Incorrect State Input.')

    for item in shopping_cart:
        tax = sales_tax
        if type(item.name) is not str or type(item.price) is not float or type(item.type) is not str:
            raise TypeError('Incorrect item data fields.')

        if item.type == 'WIC Eligible Food': tax = 0.00
        elif item.type == 'Clothing':
            if state == 'PA': tax = 0.00
            elif 'fur' not in item.name and state == 'NJ': tax = 0.00
        elif item.type != 'everything else': raise ValueError('Incorrect item type.')

        item_cost = item.price + item.price * tax
        total_cost = total_cost + item_cost
    return total_cost


if __name__ == '__main__':
    cart = []
    cart.append(ItemStock('furs', 10.00, 'Clothing'))
    cart.append(ItemStock('shirt', 10.00, 'Clothing'))
    cart.append(ItemStock('furs', 10.00, 'everything else'))
    cart.append(ItemStock('furs', 10.00, 'WIC Eligible Food'))
    x = total_cost_including_tax('DE', cart)
    print(x)
