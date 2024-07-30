# write your solution here
# # write your solution here
file_name1 = input("Student information: ")
file_name2 = input("Exercises completed: ")
file_name3 = input("Exam final_point: ")
# file_name1 = "students1.csv"
# file_name2 = "exercises1.csv"
# file_name3 = "exam_points1.csv"

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

exam = {}
with open(file_name3) as file:
    for line in file:
        line = line.replace("\n", "")
        parts = line.split(";")
        if parts[0] == "id":
            continue
        exam[parts[0]] = sum(map(int, parts[1:4]))
        

print(f"{'name':30}{'exec_nbr':<10}{'exec_pts.':<10}{'exm_pts.':<10}{'tot_pts.':<10}{'grade':<10}")

for id, name in students.items():
    if id in exercise:
        exercise_complete = exercise[id]
        exam_complete = exam[id]
        calculate = exercise_complete // 4
        final_point = exam_complete + calculate
        grade = 0
        
        if 0 <= final_point <= 14:
            grade = 0  # Fail
        elif 15 <= final_point <= 17:
            grade =  1
        elif 18 <= final_point <= 20:
            grade = 2
        elif 21 <= final_point <= 23:
            grade = 3
        elif 24 <= final_point <= 27:
            grade =  4
        else:
            grade = 5
        print(f"{name:30}{exercise_complete:<10}{calculate:<10}{exam_complete:<10}{final_point:<10}{grade:<10}")
    else:
        print("Not found.")
