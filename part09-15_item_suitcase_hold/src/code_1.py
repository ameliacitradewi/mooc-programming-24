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
        current_weight = sum(i.weight() for i in self.items)
        if current_weight + item.weight() <= self.max_weight:
            self.items.append(item)

    def weight(self):
        total_weight = sum(i.weight() for i in self.items)
        return total_weight

    def __str__(self):
        if not self.items:
            return f"0 items (0 kg)"
        else:  
            word = "item" if len(self.items) <= 1 else "items"
            total_weight = sum(i.weight() for i in self.items)
            return f"{len(self.items)} {word} ({total_weight} kg)"

    def print_items(self):
        for item in self.items:
            print(item)

    def heaviest_item(self):
        if not self.items:
            return None
        heaviest = self.items[0]
        for item in self.items:
            if item.weight() > heaviest.weight():
                heaviest = item
        return heaviest

class CargoHold:
    def __init__(self, max_cargo: int):
        self.max_cargo = max_cargo
        self.suitcases = []
    
    def max_cargo(self):
        return self.max_cargo

    def add_suitcase(self, suitcase: Suitcase):
        weight_suitcases = sum(i.weight() for i in self.suitcases)
        if weight_suitcases + suitcase.weight() <= self.max_cargo:
            self.suitcases.append(suitcase)

    def __str__(self):
        if not self.suitcases:
            return f"0 suitcases, space for {self.max_cargo} kg"
        else:                
            weight_suitcases = sum(i.weight() for i in self.suitcases)
            remaining = self.max_cargo - weight_suitcases
            word = "suitcase" if len(self.suitcases) <= 1 else "suitcases"
            return f"{len(self.suitcases)} {word}, space for {remaining} kg"

    def print_items(self):
        for suitcase in self.suitcases:
            for item in suitcase.items:
                print(item)