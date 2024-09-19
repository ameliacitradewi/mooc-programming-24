# WRITE YOUR SOLUTION HERE:
import pygame
import random
import sys

pygame.init()
window = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Asteroid Collector")

# Load images
robot = pygame.image.load("robot.png")
asteroid = pygame.image.load("rock.png")
robot_width, robot_height = robot.get_size()
asteroid_width, asteroid_height = asteroid.get_size()

# Initial positions and variables
x = 320 - robot_width // 2
y = 480 - robot_height
asteroids = []
score = 0
missed_asteroids = 0
clock = pygame.time.Clock()
fall_speed = 5

# Font for score
font = pygame.font.Font(None, 36)

def spawn_asteroid():
    x = random.randint(0, 640 - asteroid_width)
    y = -asteroid_height
    return x, y

def game_over():
    pygame.quit()
    sys.exit()

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x -= 20
                if x < 0:
                    x = 0
            if event.key == pygame.K_RIGHT:
                x += 20
                if x > 640 - robot_width:
                    x = 640 - robot_width

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Update asteroid positions
    for i, (ax, ay) in enumerate(asteroids):
        ay += fall_speed
        if ay > 480:
            missed_asteroids += 1
            if missed_asteroids >= 3:  # End game after missing 3 asteroids
                game_over()
            asteroids.pop(i)
        else:
            asteroids[i] = (ax, ay)

    # Check for collisions
    for ax, ay in asteroids:
        if x < ax + asteroid_width and x + robot_width > ax and y < ay + asteroid_height and y + robot_height > ay:
            score += 1
            asteroids.remove((ax, ay))

    # Add new asteroids
    if random.randint(1, 20) == 1:
        asteroids.append(spawn_asteroid())

    # Draw everything
    window.fill((0, 0, 0))
    window.blit(robot, (x, y))
    for ax, ay in asteroids:
        window.blit(asteroid, (ax, ay))

    # Draw score
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    window.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(30)
