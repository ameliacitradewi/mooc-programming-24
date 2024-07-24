# Write your solution here
def factorials(n: int) -> dict:
  def factorial(num: int) -> int:
      if num == 0 or num == 1:
          return 1
      result = 1
      for i in range(2, num + 1):
          result *= i
      return result
  
  factorial_dict = {}
  for i in range(1, n + 1):
      factorial_dict[i] = factorial(i)
  
  return factorial_dict
