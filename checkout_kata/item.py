# item.py

class Item:
    def __init__(self, code, price) -> None:
        self.code = code
        self.price = price

    def __eq__(self, other):
        if isinstance(other, Item):
            return self.code == other.code and self.price == other.price
        return False

    def __hash__(self):
        return hash((self.code, self.price))


# class SpecialOffer:
#     def __init__(self, item, quantity, special_price):
#         self.item = item
#         self.quantity = quantity
#         self.special_price = special_price

#     def apply_special_offer(self, items, item_code):
#         for i in range(self.quantity):
#             item_index = next((index for index, item in enumerate(
#                 items) if item.code == item_code), None)

#             if item_index is not None:
#                 items.pop(item_index)
#                 items.insert(item_index, Item(item_code, self.special_price))
