# Write your solution here
# If you use the classes made in the previous exercise, copy them here
class Book:
    _id = 1

    def __init__(self, description, programmer, workload):
        self.description = description
        self.programmer = programmer
        self.workload = workload
        self.id = Book._id
        Book._id += 1
        self._is_finished = False
    
    def is_finished(self):
        return self._is_finished

    def mark_as_finished(self):
        self._is_finished = True
    
    def __str__(self):
        status = "FINISHED" if self.is_finished() else "NOT FINISHED"
        return f"{self.id}: {self.description} ({self.workload} hours), programmer {self.programmer} {status}"

class BookOrder:
    def __init__(self):
        self.orders = []

    def add_order(self, description, programmer, workload):
        new_book = Book(description, programmer, workload)
        self.orders.append(new_book)
        print("added!")
    
    def list_unfinished(self):
        list_unfinished = [order for order in self.orders if not order.is_finished()]
        print('\n'.join(str(order) for order in list_unfinished) or "no unfinished tasks")

    def list_finished(self):
        list_finished = [order for order in self.orders if order.is_finished()]
        print('\n'.join(str(order) for order in list_finished) or "no finished tasks")

    def mark_as_finished(self, id):
        for order in self.orders:
            if order.id == id:
                order.mark_as_finished()
                print("marked as finished")        
                return
        print("erroneous input")                

    def programmers(self):
        list_programmers = list(set(order.programmer for order in self.orders))
        print('\n'.join(str(programmer) for programmer in list_programmers) or "erroneous input")

    def status_of_programmer(self, programmer):
        finished = 0
        not_finished = 0
        hours_done = 0
        hours_to_go = 0

        for order in self.orders:
            if order.programmer == programmer:
                if order.is_finished():
                    finished += 1
                    hours_done += order.workload
                else:
                    not_finished += 1
                    hours_to_go += order.workload

        if finished == 0 and not_finished == 0:
            print("erroneous input")
        else:
            print(f"tasks: finished {finished} not finished {not_finished}, hours: done {hours_done} scheduled {hours_to_go}")
    
class BookApplication:
    def __init__(self):
        self.book_order = BookOrder()

    def help(self):
        print("commands:")
        print("0 exit")
        print("1 add order")
        print("2 list finished tasks")
        print("3 list unfinished tasks")
        print("4 mark task as finished")
        print("5 programmers")
        print("6 status of programmer")

    def add_entry_order(self):
        description = input("description: ")
        progwork = input("programmer and workload estimate: ")
        parts = progwork.split()
        if len(parts) != 2:
            print("erroneous input")
            return
        programmer = parts[0]
        try:
            workload = int(parts[1])
        except ValueError:
            print("erroneous input")
            return
        self.book_order.add_order(description, programmer, workload)

    def execute(self):
        self.help()

        while True:
            print("")
            command = input("Command: ")
            if command == "0":
                break
            elif command == "1":
                self.add_entry_order()
            elif command == "2":
                self.book_order.list_finished()
            elif command == "3":
                self.book_order.list_unfinished()
            elif command == "4":
                try:
                    id = int(input("id: "))
                    self.book_order.mark_as_finished(id)
                except ValueError:
                    print("erroneous input")
            elif command == "5":
                self.book_order.programmers()
            elif command == "6":
                programmer = input("programmer: ")
                self.book_order.status_of_programmer(programmer)
            else:
                print("erroneous input")

# Testing Case
application = BookApplication()
application.execute()