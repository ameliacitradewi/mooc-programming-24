# Write your solution here
import csv
from datetime import datetime, timedelta

def final_points():
    start_times = {}
    submissions = {}

    with open('start_times.csv', 'r') as f:
        reader = csv.reader(f, delimiter=';')
        for row in reader:
            name, start_time = row
            start_times[name] = datetime.strptime(start_time, '%H:%M')

    with open('submissions.csv', 'r') as f:
        reader = csv.reader(f, delimiter=';')
        for row in reader:
            name, task, points, submission_time = row
            task = int(task)
            points = int(points)
            submission_time = datetime.strptime(submission_time, '%H:%M')
            start_time = start_times[name]
            time_diff = submission_time - start_time

            # Check if the submission is within the allowed time frame
            if time_diff <= timedelta(hours=3):
                if name not in submissions:
                    submissions[name] = {}
                if task not in submissions[name]:
                    submissions[name][task] = points
                else:
                    submissions[name][task] = max(submissions[name][task], points)

    # Calculate the total points for each student
    final_scores = {}
    for name, tasks in submissions.items():
        final_scores[name] = sum(tasks.values())

    return final_scores

# Example usage
# print(final_points())