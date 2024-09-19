# WRITE YOUR SOLUTION HERE:
import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")
robot_width = robot.get_width()
robot_height = robot.get_height()

# Define the number of robots
num_robots = 10

# Create a list to store robots' data
robots = []

# Initialize robots with random positions and velocities
for _ in range(num_robots):
    x = random.randint(0, window_width - robot_width)
    y = random.randint(-window_height, 0)
    velocity_y = random.uniform(1.0, 3.0)
    velocity_x = random.uniform(1.0, 2.0) * random.choice([-1, 1])
    robots.append({'x': x, 'y': y, 'velocity_x': velocity_x, 'velocity_y': velocity_y, 'falling': True})

# Set up the clock for frame rate control
clock = pygame.time.Clock()

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update robot positions
    for robot_data in robots:
        if robot_data['falling']:
            # Update falling position
            robot_data['y'] += robot_data['velocity_y']
            if robot_data['y'] >= window_height - robot_height:
                # Hit the ground
                robot_data['falling'] = False
                robot_data['velocity_y'] = 0
                # Randomize horizontal direction
                robot_data['velocity_x'] = random.uniform(1.0, 2.0) * random.choice([-1, 1])
        else:
            # Move horizontally
            robot_data['x'] += robot_data['velocity_x']
            if robot_data['x'] < -robot_width or robot_data['x'] > window_width:
                # Remove robot if it goes off screen
                robots.remove(robot_data)

    # Fill the window with black
    window.fill((0, 0, 0))

    # Draw robots
    for robot_data in robots:
        window.blit(robot, (robot_data['x'], robot_data['y']))

    # Update the display
    pygame.display.flip()

    # Control the frame rate
    clock.tick(60)