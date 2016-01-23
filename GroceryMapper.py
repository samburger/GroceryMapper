"""
MVP: define a data structure for store, aisle, items
GroceryStore has a certain number of GroceryAisles which contain GroceryItems.
Aisles are numbered from one side of the store to another.
Given a list of items (ShoppingList), return the list ordered such that
the items can be found in increasing store aisles.
"""


class ShoppingList():

    def __init__(self, item_list=[]):
        self.item_list = item_list

    def add(self, item):
        if item not in self.item_list:
            self.item_list.append(item)

    def remove(self, item):
        if item in self.item_list:
            self.item_list.remove(item)

    def sort_list(self, store):
        final_list = []
        for item in self.item_list:
            for aisle in store.aisle_list:
                if item in aisle.item_list:
                    final_list.append((item.name, aisle.number))
                    break
                    # TODO: handle item not in any aisles.  ask to add?
        return [i[0] for i in sorted(final_list, key=lambda x: x[1])]


class GroceryItem():

    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        return self.name == other.name


class GroceryAisle():

    def __init__(self, number):
        self.number = number
        self.item_list = []

    def add(self, item):
        if item not in self.item_list:
            self.item_list.append(item)

    def remove(self, item):
        if item in self.item_list:
            self.item_list.remove(item)


class GroceryStore():

    def __init__(self, num_aisles):
        self.num_aisles = num_aisles
        self.aisle_list = []
        for i in range(1, self.num_aisles + 1):
            self.aisle_list.append(GroceryAisle(i))

    def stock_aisle(self, stock):
        self.aisle_list[stock[1] - 1].item_list.append(GroceryItem(stock[0]))

    # TODO: handle inserting aisles, which should re-number existing aisles.
