# Write your solution here
# result = []

# while True:
#     user_input = input("Exam points and exercises completed: ")
        
#     if user_input == "":
#         break

#     exam_point, exer_completed = map(int, user_input.split())
#     exer_point = exer_completed // 10
#     total_point = exam_point + exer_point

#     result.append((exam_point, exer_point))


# def get_grade(exam_point, total_point):
#     if exam_point < 10:
#             grade = 0
#     else:
#         if total_point in range(0, 15):
#             grade = 0
#         elif total_point in range(15, 18):
#             grade = 1
#         elif total_point in range(18, 21):
#             grade = 2
#         elif total_point in range(21, 24):
#             grade = 3
#         elif total_point in range(24, 28):
#             grade = 4
#         else:
#             grade = 5

def get_grade(exam_points, exercise_points):
    total_points = exam_points + exercise_points
    if exam_points < 10:
        return 0
    elif total_points <= 14:
        return 0
    elif total_points <= 17:
        return 1
    elif total_points <= 20:
        return 2
    elif total_points <= 23:
        return 3
    elif total_points <= 27:
        return 4
    else:
        return 5

results = []

while True:
    user_input = input("Exam points and exercises completed: ")
    if user_input == "":
        break

    exam_points, exercises_completed = map(int, user_input.split())
    exercise_points = exercises_completed // 10
    results.append((exam_points, exercise_points))


# Calculate statistics
total_students = len(results)
total_points = [exam + exercise for exam, exercise in results]
passing_students = [points for exam, points in results if exam >= 10 and (exam + points) >= 15]

# Average of points
average_points = sum(total_points) / total_students

# Pass percentage
pass_percentage = (len(passing_students) / total_students) * 100

# Grade distribution
grade_counts = [0] * 6  # Grades 0 to 5
for exam, exercise in results:
    grade = get_grade(exam, exercise)
    grade_counts[grade] += 1

# Print statistics
print("Statistics:")
print(f"Points average: {average_points:.1f}")
print(f"Pass percentage: {pass_percentage:.1f}")
print("Grade distribution:")
for grade in range(5, -1, -1):
    stars = '*' * grade_counts[grade]
    print(f"  {grade}: {stars}")