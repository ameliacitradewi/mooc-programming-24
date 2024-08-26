# WRITE YOUR SOLUTION HERE:
class Person:
    def __init__(self, name: str, height: int):
        self.name = name
        self.height = height

    def __str__(self):
        return self.name

class Room:
    def __init__(self):
        self.person = []
    
    def add(self, person: Person):
        self.person.append(person)
    
    def is_empty(self):
        return len(self.person) == 0

    def print_contents(self):
        total_height = sum(person.height for person in self.person)
        print(f"There are {len(self.person)} persons in the room, and their combined height is {total_height} cm")
        for person in self.person:
            print(f"{person} ({person.height} cm)")

    def shortest(self):
        if self.is_empty():
          return None
        return min(self.person, key=lambda person: person.height)

    def remove_shortest(self):
        shortest_person = self.shortest()
        if shortest_person:
            self.person.remove(shortest_person)
        return shortest_person

# Example Usage
room = Room()

room.add(Person("Lea", 183))
room.add(Person("Kenya", 172))
room.add(Person("Nina", 162))
room.add(Person("Ally", 166))
room.print_contents()

print()

removed = room.remove_shortest()
print(f"Removed from room: {removed.name}")

print()

room.print_contents()