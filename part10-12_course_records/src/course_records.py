# Write your solution here:
class Course:
    def __init__(self, name: str, grade: int, credits: int):
        self.name = name
        self.grade = grade
        self.credits = credits

    def update_grade(self, new_grade: int):
        if new_grade > self.grade:
            self.grade = new_grade

class CourseRecords:
    def __init__(self):
        self.courses = {}

    def add_courses(self, name: str, grade: int, credits: int):
        if name not in self.courses:
            self.courses[name] = Course(name, grade, credits)
        else:
            self.courses[name].update_grade(grade)

    def get_courses(self, name: str):
        if name in self.courses:
            course = self.courses[name]
            return f"{course.name} ({course.credits} cr) grade {course.grade}"
        return "no entry for this course"        

    def statistics(self):
        if not self.courses:
            return "You are not taking any courses yet."
        
        total_courses = len(self.courses)
        total_credits = sum(course.credits for course in self.courses.values())
        mean_grade = sum(course.grade for course in self.courses.values()) / total_courses

        # Grade distribution
        grade_distribution = {5: 0, 4: 0, 3: 0, 2: 0, 1: 0}
        for course in self.courses.values():
            grade_distribution[course.grade] += 1

        # Building statistics output
        result = f"{total_courses} completed courses, a total of {total_credits} credits\n"
        result += f"mean {mean_grade:.1f}\n"
        result += "grade distribution\n"
        for grade in range(5, 0, -1):
            result += f"{grade}: {'x' * grade_distribution[grade]}\n"
        
        return result.strip()

class CourseApplication:
    def __init__(self):
        self.course_records = CourseRecords()

    def help(self):
        print("1 add course")
        print("2 get course data")
        print("3 statistics")
        print("0 exit")

    def add_courses(self):
        name = input("course: ")
        grade = int(input("grade: "))
        credits = int(input("credits: "))
        self.course_records.add_courses(name, grade, credits)

    def get_courses(self):
        name = input("course: ")
        print(self.course_records.get_courses(name))

    def statistics(self):
        print(self.course_records.statistics())

    def execute(self):
        self.help()
        while True:
            print("")
            command = input("command: ")
            if command == "0":
                break
            elif command == "1":
                self.add_courses()
            elif command == "2":
                self.get_courses()
            elif command == "3":
                self.statistics()
            else:
                self.help()

# Running the application
application = CourseApplication()
application.execute()
        
