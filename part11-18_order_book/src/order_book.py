# Write your solution here:
class Task:
    _id = 1

    def __init__(self, description, programmer, workload):
        self.description = description
        self.programmer = programmer
        self.workload = workload
        self.id = Task._id
        Task._id += 1
        self._is_finished = False     

    def is_finished(self):
        return self._is_finished
    
    def mark_finished(self):
        self._is_finished = True
    
    def __str__(self):
        status = "FINISHED" if self.is_finished() else "NOT FINISHED"
        return f"{self.id}: {self.description} ({self.workload} hours), programmer {self.programmer} {status}"

class OrderBook:
    def __init__(self):
        self.orders = []
    
    def add_order(self, description, programmer, workload):
        new_task = Task(description, programmer, workload)
        self.orders.append(new_task)

    def all_orders(self):
        return self.orders

    def programmers(self):
        return list(set(order.programmer for order in self.orders))

    def mark_finished(self, id: int):
        for order in self.orders:
            if order.id == id:
                order.mark_finished()
                return
        raise ValueError("There is no such id")

    def finished_orders(self):
        return [order for order in self.orders if order.is_finished()]

    def unfinished_orders(self):
        return [order for order in self.orders if not order.is_finished()]

    def status_of_programmer(self, programmer: str):
        finished_tasks = 0
        unfinished_tasks = 0
        finished_hours = 0
        unfinished_hours = 0

        for order in self.orders:
            if order.programmer == programmer:
                if order.is_finished():
                    finished_tasks += 1
                    finished_hours += order.workload
                else:
                    unfinished_tasks += 1
                    unfinished_hours += order.workload

        if finished_tasks == 0 and unfinished_tasks == 0:
            raise ValueError("There is no such programmer")

        return (finished_tasks, unfinished_tasks, finished_hours, unfinished_hours)

# Example usage
orders = OrderBook()
orders.add_order("program webstore", "Adele", 10)
orders.add_order("program mobile app for workload accounting", "Adele", 25)
orders.add_order("program app for practising mathematics", "Adele", 100)
orders.add_order("program the next facebook", "Eric", 1000)

orders.mark_finished(1)
orders.mark_finished(2)

status = orders.status_of_programmer("Adele")
print(status)  # Should output (2, 1, 35, 100)