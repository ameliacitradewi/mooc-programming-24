# Write your solution here
import csv
from datetime import datetime, timedelta

def cheaters():
    start_times = {}
    cheaters_list = set()

    with open('start_times.csv', 'r') as file:
        reader = csv.reader(file, delimiter=';')
        for row in reader:
            name, start_time = row
            start_times[name] = datetime.strptime(start_time, '%H:%M')

    with open('submissions.csv', 'r') as file:
        reader = csv.reader(file, delimiter=';')
        for row in reader:
            name, task, points, submission_time = row
            submission_time = datetime.strptime(submission_time, '%H:%M')
            start_time = start_times[name]
            time_diff = submission_time - start_time

            # Check if the time difference is greater than 3 hours
            if time_diff > timedelta(hours=3):
                cheaters_list.add(name)

    return list(cheaters_list)

# Example usage
# print(cheaters())