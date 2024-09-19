# # WRITE YOUR SOLUTION HERE:
import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")

x = 0
y = 0
velocity_x = 2
velocity_y = 0
clock = pygame.time.Clock()

window_width = 640
window_height = 480

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    # Position update
    if direction == 'right':
        x += velocity_x
        if x + robot.get_width() >= window_width:
            direction = 'down'
    elif direction == 'down':
        y += velocity_y
        if y + robot.get_height() >= window_height:
            direction = 'left'
    elif direction == 'left':
        x -= velocity_x
        if x <= 0:
            direction = 'up'
    elif direction == 'up':
        y -= velocity_y
        if y <= 0:
            direction = 'right'

    window.fill((0, 0, 0))
    window.blit(robot, (x, y))
    pygame.display.flip()

    clock.tick(60)