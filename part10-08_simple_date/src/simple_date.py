# WRITE YOUR SOLUTION HERE:
class SimpleDate:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def __str__(self):
        return f"{self.day}.{self.month}.{self.year}"
    
    def self_date(self):
        return (self.day, self.month, self.year)

    def total_day_from_date(self):
        return self.day + (self.month * 30) + (self.year * 12 * 30)
    
    def __eq__(self, another):
        return self.self_date() == another.self_date()

    def __ne__(self, another):
        return not self.__eq__(another)

    def __lt__(self, another):
        total_day = self.total_day_from_date()
        another_total_day = another.total_day_from_date()
        return total_day < another_total_day

    def __gt__(self, another):
        total_day = self.total_day_from_date()
        another_total_day = another.total_day_from_date()
        return total_day > another_total_day

    def __add__(self, days):
        day = self.day + days
        month = self.month
        year = self.year

        # Calculate the number of months to add
        month += (day - 1) // 30
        day = (day - 1) % 30 + 1

        # Calculate the number of years to add
        year += (month - 1) // 12
        month = (month - 1) % 12 + 1

        return SimpleDate(day, month, year)

    def __sub__(self, another):
        total_day = self.total_day_from_date()
        another_total_day = another.total_day_from_date()
        return abs(total_day - another_total_day)
