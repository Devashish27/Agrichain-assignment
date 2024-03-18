# special_offer.py

from item import Item


class SpecialOffer:
    def __init__(self, item, quantity, special_price):
        self.item = item
        self.quantity = quantity
        self.special_price = special_price

    def apply_special_offer(self, items, item_code):
        for i in range(self.quantity):
            item_index = next((index for index, item in enumerate(
                items) if item.code == item_code), None)

            if item_index is not None:
                items.pop(item_index)

        items.insert(item_index, Item(item_code, self.special_price))
