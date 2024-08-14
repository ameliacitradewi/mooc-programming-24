# Write your solution here
def smallest_average(person1: dict, person2: dict, person3: dict) -> dict:
    # Calculate the average for each person
    def calculate_average(person: dict) -> float:
        return (person["result1"] + person["result2"] + person["result3"]) / 3

    # Calculate averages
    avg1 = calculate_average(person1)
    avg2 = calculate_average(person2)
    avg3 = calculate_average(person3)

    # Determine the person with the smallest average
    if avg1 < avg2 and avg1 < avg3:
        return person1
    elif avg2 < avg1 and avg2 < avg3:
        return person2
    else:
        return person3

# # Example usage
# person1 = {"name": "Mary", "result1": 2, "result2": 3, "result3": 3}
# person2 = {"name": "Gary", "result1": 5, "result2": 1, "result3": 8}
# person3 = {"name": "Larry", "result1": 3, "result2": 1, "result3": 1}

# print(smallest_average(person1, person2, person3))