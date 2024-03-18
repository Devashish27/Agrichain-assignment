import unittest
from item import Item
from special_offer import SpecialOffer
from checkout import Checkout


class TestCheckout(unittest.TestCase):
    def setUp(self):
        self.checkout = Checkout()

    def test_add_item(self):
        self.checkout.add_item(Item('A', 50))
        self.assertEqual(len(self.checkout.items), 1)

    def test_apply_special_offers(self):
        item_a = Item('A', 50)
        special_offer_a = SpecialOffer(item_a, 3, 130)

        self.checkout.special_offers = {'A': special_offer_a}

        for _ in range(5):
            self.checkout.add_item(item_a)

        print("Items before special offers:", self.checkout.items)

        self.checkout.apply_special_offers()

        print("Items after special offers:", self.checkout.items)

        # Calculate the expected total price after applying special offers
        # 130 for special_offer_a + 50 for the remaining item A
        expected_total_price = 130 + 50 * 2
        actual_total_price = sum(item.price for item in self.checkout.items)
        self.assertEqual(actual_total_price, expected_total_price)

    def test_calculate_total(self):
        item_a = Item('A', 50)
        item_b = Item('B', 30)

        for _ in range(3):
            self.checkout.add_item(item_a)
            self.checkout.add_item(item_b)

        total_price = self.checkout.calculate_total()

        self.assertEqual(total_price, 3 * item_a.price + 3 * item_b.price)


if __name__ == '__main__':
    unittest.main()
