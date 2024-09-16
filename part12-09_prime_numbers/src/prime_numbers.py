# Write your solution here
def prime_numbers():
    numbers = 2
    while True:
        if all(numbers % i != 0 for i in range(2, int(numbers**0.5) + 1)):
            yield numbers
        numbers += 1

# Example Usage
numbers = prime_numbers()
for i in range(8):
    print(next(numbers))