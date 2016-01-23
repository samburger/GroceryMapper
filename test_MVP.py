"""
Test the MVP goal of returning shopping list sorted by store aisle.
"""
import unittest
from GroceryMapper import *


class SortShoppingListTest(unittest.TestCase):

    def setUp(self):
        # Make grocery store of 5 aisles.
        self.store = GroceryStore(5)
        # Make shopping list
        test_items = ["Apple", "Pork", "Bread", "Sausage",
                      "Soup", "Rice", "Lettuce"]
        self.shoppinglist = ShoppingList([GroceryItem(n) for n in test_items])
        # Add items to each aisle.
        stock_list = list(zip(test_items, [1, 3, 2, 3, 4, 5, 1]))
        for i in stock_list:
            self.store.stock_aisle(i)

    def test_sortlist(self):
        self.assertEqual(self.shoppinglist.sort_list(self.store),
                         ["Apple", "Lettuce", "Bread", "Pork",
                          "Sausage", "Soup", "Rice"],
                          "List sorted incorrectly")


if __name__ == '__main__':
    unittest.main()
