# write your solution here
file_name1 = input("Student information: ")
file_name2 = input("Exercises completed: ")

students = {}
with open(file_name1) as file:
    for line in file:
        line = line.replace("\n", "")
        parts = line.split(";")
        if parts[0] == "id":
            continue
        students[parts[0]] = parts[1] + " " + parts[2]

exercise = {}
with open(file_name2) as file:
    for line in file:
        line = line.replace("\n", "")
        parts = line.split(";")
        if parts[0] == "id":
            continue
        # exercise[parts[0]] = int(parts[1]) + int(parts[2]) + int(parts[3]) + int(parts[4]) + int(parts[5]) + int(parts[6]) + int(parts[7])
        exercise[parts[0]] = sum(map(int, parts[1:8]))

for id, name in students.items():
    if id in exercise:
        scores = exercise[id]
        print(f"{name} {scores}")
    else:
        print("Not found.")
