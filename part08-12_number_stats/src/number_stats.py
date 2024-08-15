# Write your solution here!
class NumberStats:
  def __init__(self):
      self.numbers = 0
      self.sum = 0

  def add_number(self, number: int):
      self.numbers += 1
      self.sum += number

  def count_numbers(self):
      return self.numbers

  def get_sum(self):
      return self.sum

  def average(self):
      if self.numbers == 0:
          return 0
      return self.sum / self.numbers

stats = NumberStats()
even = NumberStats()
odd = NumberStats()
print("Please type in integer numbers:")

while True:
    numbers = int(input())
    if numbers == -1:
        break
    stats.add_number(numbers)
    if numbers % 2 == 0:
        even.add_number(numbers)
    else:
        odd.add_number(numbers)

print("Sum of numbers:", stats.get_sum())
print("Mean of numbers:", stats.average())
print("Sum of even numbers:", even.get_sum())
print("Sum of odd numbers:", odd.get_sum())