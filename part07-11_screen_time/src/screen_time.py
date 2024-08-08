# Write your solution here
from datetime import datetime, timedelta

filename = input()
start_date_str = input()
days_to_add = int(input())

start_date = datetime.strptime(start_date_str, "%d.%m.%Y")
end_date = start_date + timedelta(days=days_to_add-1)
screen_time = {}

for day in range(days_to_add):
    current_date = start_date + timedelta(days=day)
    duration = input(f'Screen time {current_date.strftime("%d.%m.%Y")}: ')
    screen_time[current_date.strftime("%d.%m.%Y")] = duration
print("Data stored in file", filename)

total_screen_time = 0

for value in screen_time.values():
    minutes = value.split()
    total_screen_time += sum(int(minute) for minute in minutes)

average_minutes = total_screen_time / days_to_add

with open(filename, 'w') as file:
    file.write(f"Time period: {start_date.strftime('%d.%m.%Y')}-{end_date.strftime('%d.%m.%Y')}\n")
    file.write(f"Total minutes: {total_screen_time}\n")
    file.write(f"Average minutes: {average_minutes}\n")
    for key, value in screen_time.items():
        file.write(f"{key}: {value.replace(' ', '/')}\n")