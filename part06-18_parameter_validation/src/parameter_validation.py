# Write your solution here
def new_person(name: str, age: int):
    name_split = " " in name
    if name == "" or len(name) > 40 or name_split == False:
        raise ValueError("Name should be more than 2 words and shorter than 40 char.")
    elif age <= 0 or age > 150:
        raise ValueError("Are you sure that is your age?")
    else:
        person = (name, age)
    return person
