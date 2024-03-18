# checkout.py

from collections import Counter
from item import Item


class Checkout:
    def __init__(self) -> None:
        self.items = []
        self.special_offers = {}

    def add_item(self, item):
        self.items.append(item)

    def apply_special_offers(self):
        for item, count in Counter(self.items).items():
            if item.code in self.special_offers:
                special_offer = self.special_offers[item.code]
                special_price_items_count = count // special_offer.quantity

                for i in range(special_price_items_count):
                    special_offer.apply_special_offer(self.items, item.code)

    def calculate_total(self):
        total = 0
        for item in self.items:
            total += item.price
        return total
