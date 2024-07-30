# Write your solution here
def add_student(students, name):
  if name not in students:
      students[name] = []

def print_student(students, name):
  if name in students:
      print(f"{name}:")
      if not students[name]:
          print(" no completed courses")
      else:
          print(f" {len(students[name])} completed courses:")
          for course, grade in students[name]:
              print(f"  {course} {grade}")
          average_grade = sum(grade for course, grade in students[name]) / len(students[name])
          print(f" average grade {average_grade:.1f}")
  else:
      print(f"{name}: no such person in the database")

def add_course(students, name, course_info):
  if name in students:
      course_name, grade = course_info
      if grade == 0:
          return
      for i, (existing_course, existing_grade) in enumerate(students[name]):
          if existing_course == course_name:
              if grade > existing_grade:
                  students[name][i] = (course_name, grade)
              return
      students[name].append(course_info)

def summary(students):
  print(f"students {len(students)}")
  
  most_courses = 0
  most_courses_student = ""
  best_average = 0
  best_average_student = ""
  
  for student, courses in students.items():
      if len(courses) > most_courses:
          most_courses = len(courses)
          most_courses_student = student
      
      if courses:
          average_grade = sum(grade for course, grade in courses) / len(courses)
          if average_grade > best_average:
              best_average = average_grade
              best_average_student = student
  
  if most_courses_student:
      print(f"most courses completed {most_courses} {most_courses_student}")
  if best_average_student:
      print(f"best average grade {best_average:.1f} {best_average_student}")

# Example usage
# students = {}
# add_student(students, "Peter")
# add_student(students, "Eliza")
# add_course(students, "Peter", ("Data Structures and Algorithms", 1))
# add_course(students, "Peter", ("Introduction to Programming", 1))
# add_course(students, "Peter", ("Advanced Course in Programming", 1))
# add_course(students, "Eliza", ("Introduction to Programming", 5))
# add_course(students, "Eliza", ("Introduction to Computer Science", 4))
# summary(students)