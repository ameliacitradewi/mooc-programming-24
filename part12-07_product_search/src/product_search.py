# Write your solution here
def search(products: list, criterion: callable):
    return [product for product in products if criterion(product)]

def price_under_4_euros(product):
    return product[1] < 4

# Example Usage
products = [("banana", 5.95, 12), ("apple", 3.95, 3), ("orange", 4.50, 2), ("watermelon", 4.95, 22), ("kale", 0.99, 1)]
for product in search(products, price_under_4_euros):
    print(product)
    # Output:
    # ('apple', 3.95, 3)
    # ('kale', 0.99, 1)

for product in search(products, lambda t: t[2]>10):
    print(product)
    # lambda function no need to define in the solution
    # Output:
    # ('banana', 5.95, 12)
    # ('watermelon', 4.95, 22)
