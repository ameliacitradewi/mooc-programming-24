# WRITE YOUR SOLUTION HERE:
import tkinter as tk
import time
import math

def update_clock():
  # Get the current time
  current_time = time.strftime('%H:%M:%S')
  label.config(text=current_time)

  # Get the current hour, minute, and second
  hour = int(time.strftime('%I'))
  minute = int(time.strftime('%M'))
  second = int(time.strftime('%S'))

  # Calculate the angles for the hands
  second_angle = math.radians(second * 6 - 90)
  minute_angle = math.radians(minute * 6 - 90)
  hour_angle = math.radians((hour % 12) * 30 + minute * 0.5 - 90)

  # Calculate the hand positions
  second_hand = (center_x + second_length * math.cos(second_angle),
                 center_y + second_length * math.sin(second_angle))
  minute_hand = (center_x + minute_length * math.cos(minute_angle),
                 center_y + minute_length * math.sin(minute_angle))
  hour_hand = (center_x + hour_length * math.cos(hour_angle),
               center_y + hour_length * math.sin(hour_angle))

  # Draw the hands
  canvas.delete('hands')
  canvas.create_line(center_x, center_y, *second_hand, fill='blue', width=1, tag='hands')
  canvas.create_line(center_x, center_y, *minute_hand, fill='blue', width=2, tag='hands')
  canvas.create_line(center_x, center_y, *hour_hand, fill='blue', width=3, tag='hands')

  # Update every 1000 ms (1 second)
  root.after(1000, update_clock)

# Create the main window
root = tk.Tk()
root.title('Clock')

# Create a label to display the time
label = tk.Label(root, font=('calibri', 20, 'bold'), background='black', foreground='white')
label.pack(anchor='n')

# Create a canvas for the clock face
canvas = tk.Canvas(root, width=400, height=400, bg='black')
canvas.pack()

# Center of the clock
center_x, center_y = 200, 200

# Lengths of the hands
second_length = 180
minute_length = 150
hour_length = 100

# Draw the clock face
canvas.create_oval(center_x - 190, center_y - 190, center_x + 190, center_y + 190, outline='red', width=3)

# Start the clock
update_clock()

# Run the application
root.mainloop()