from item import Item
from special_offer import SpecialOffer
from checkout import Checkout


def main():
    checkout = Checkout()

    # Add special offers
    checkout.special_offers = {
        'A': SpecialOffer(Item('A', 50), 3, 130),
        'B': SpecialOffer(Item('B', 30), 2, 45)
    }

    # Add Items to the cart.
    checkout.add_item(Item('A', 50))
    checkout.add_item(Item('B', 30))
    checkout.add_item(Item('A', 50))
    checkout.add_item(Item('B', 30))
    checkout.add_item(Item('A', 50))

    # Apply Special Offers..
    checkout.apply_special_offers()

    # Calculate the total price...
    total_price = checkout.calculate_total()
    print(f"Total price: {total_price}")


if __name__ == "__main__":
    main()
