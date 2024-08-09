# Write your solution here
import urllib.request
import json
import math

def retrieve_all():
    url = "https://studies.cs.helsinki.fi/stats-mock/api/courses"
    request = urllib.request.urlopen(url)
    json_format = json.loads(request.read())
    
    active_course = []
    for course in json_format:
        if course["enabled"] == True:
            full_name = course.get("fullName")
            name = course.get("name")
            year = course.get("year")
            total_exercises = sum(course["exercises"])
            active_course.append((full_name, name, year, total_exercises))
    
    return active_course

def retrieve_course(course_name: str):
    url = f"https://studies.cs.helsinki.fi/stats-mock/api/courses/{course_name}/stats"
    request = urllib.request.urlopen(url)
    json_format = json.loads(request.read())
    max_students, hours, exercises = 0, 0, 0
    result = {}
    
    for key, value in json_format.items():
        students = value.get("students", 0)
        if students > max_students:
            max_students = students

        hour = value.get("hour_total", 0)
        hours += hour

        exercise = value.get("exercise_total", 0)
        exercises += exercise
    
    result["weeks"] = len(json_format)
    result["students"] = max_students
    result["hours"] = hours
    result["hours_average"] = math.floor(hours / max_students)
    result["exercises"] = exercises
    result["exercises_average"] = math.floor(exercises / max_students)

    return result


# Example Usage
# print(retrieve_course("docker2019"))
