# Write your solution here:
class Item:
    def __init__(self, name: str, weight: int):
        self._name = name
        self._weight = weight
    
    def name(self):
        return self._name
    
    def weight(self):
        return self._weight
    
    def __str__(self):
        return f"{self._name} ({self._weight} kg)"

class Suitcase:
    def __init__(self, max_weight: int):
        self.max_weight = max_weight
        self.items = []

    def add_item(self, item = Item):
        if self.weight() + item.weight() <= self.max_weight:
            self.items.append(item)

    def weight(self):  # calculate suitcase weight
        return sum(i.weight() for i in self.items)

    def __str__(self):
        item_count = len(self.items)
        word = "item" if item_count == 1 else "items"
        return f"{item_count} {word} ({self.weight()} kg)"

    def print_items(self):
        for item in self.items:
            print(item)

    def heaviest_item(self):
        heaviest = self.items[0]
        for item in self.items:
            if item.weight() > heaviest.weight():
                heaviest = item
        return heaviest
    # another way: return max(self.items, key=lambda item: item.weight(), default=None)

class CargoHold:
    def __init__(self, max_cargo: int):
        self.max_cargo = max_cargo
        self.suitcases = []
    
    def max_cargo(self):
        return self.max_cargo
    
    def weight(self):  # calculate suitcases weight (total cargo)
        return sum(suitcase.weight() for suitcase in self.suitcases)

    def add_suitcase(self, suitcase: Suitcase):
        if self.weight() + suitcase.weight() <= self.max_cargo:
            self.suitcases.append(suitcase)

    def __str__(self):
        suitcase_count = len(self.suitcases)
        word = "suitcase" if suitcase_count == 1 else "suitcases"
        remaining_weight = self.max_cargo - self.weight()
        return f"{suitcase_count} {word}, space for {remaining_weight} kg"
        

    def print_items(self):
        for suitcase in self.suitcases:
            suitcase.print_items()  # calling method from suitcase class to print out the items