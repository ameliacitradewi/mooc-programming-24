from functools import reduce

class CourseAttempt:
    def __init__(self, course_name: str, grade: int, credits: int):
        self.course_name = course_name
        self.grade = grade
        self.credits = credits

    def __str__(self):
        return f"{self.course_name} ({self.credits} cr) grade {self.grade}"

# Write your solution
def sum_of_all_credits(attempts: list):
    return reduce(lambda total, attempt: total + attempt.credits, attempts, 0)

def sum_of_passed_credits(attempts: list):
    passed_criteria = list(filter(lambda x: x.grade > 1, attempts))
    return reduce(lambda total, attempt: attempt.credits + total, passed_criteria, 0)

def average(attempts: list):
    passed_grade = list(filter(lambda x: x.grade > 0, attempts))
    total_grade = reduce(lambda total, attempt: attempt.grade + total, passed_grade, 0)
    return total_grade / len(passed_grade)

# Example Case
s1 = CourseAttempt("Introduction to Programming", 5, 5)
s2 = CourseAttempt("Advanced Course in Programming", 4, 5)
s3 = CourseAttempt("Data Structures and Algorithms", 3, 10)
credit_sum = sum_of_passed_credits([s1, s2, s3])
print(credit_sum)
ag = average([s1, s2, s3])
print(ag)

# Eventhough this excercise could be done using recurssion,
# the task spesifically asks you to use filter and reduce