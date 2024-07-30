# Write your solution here
def oldest_person(people: list):
    oldest = people[0]
  
    for person in people:
        if person[1] < oldest[1]:  # Compare years of birth
            oldest = person
    
    return oldest[0]

# p1 = ("Adam", 1977)
# p2 = ("Ellen", 1985)
# p3 = ("Mary", 1953)
# p4 = ("Ernest", 1997)
# people = [p1, p2, p3, p4]
# print(oldest_person(people))

