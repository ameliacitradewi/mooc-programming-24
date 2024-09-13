# Write your solution here:
class Task:
    _id_counter = 1

    def __init__(self, description: str, programmer: str, workload: int):
        self.description = description
        self.programmer = programmer
        self.workload = workload
        self._is_finished = False
        self.id = Task._id_counter
        Task._id_counter += 1

    def is_finished(self) -> bool:
        return self._is_finished

    def mark_finished(self):
        self._is_finished = True

    def __str__(self):
        status = "FINISHED" if self.is_finished() else "NOT FINISHED"
        return f"{self.id}: {self.description} ({self.workload} hours), programmer {self.programmer} {status}"