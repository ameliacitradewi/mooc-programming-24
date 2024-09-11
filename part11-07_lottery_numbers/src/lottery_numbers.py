# WRITE YOUR SOLUTION HERE:
class LotteryNumbers:
    def __init__(self, week: int, correct_numbers: list):
        self.week = week
        self.correct_numbers = correct_numbers

    def number_of_hits(self, numbers: list):
        return len([num for num in numbers if num in self.correct_numbers])
    
    def hits_in_place(self, numbers: list):
        return [num if num in self.correct_numbers else -1 for num in numbers]