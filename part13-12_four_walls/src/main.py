# WRITE YOUR SOLUTION HERE:
# WRITE YOUR SOLUTION HERE:
import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")
robot_height = robot.get_height()
robot_width = robot.get_width()

x = 0
y = 480-robot_height

to_right = False
to_left = False
up = False
down = False

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_left = True
            if event.key == pygame.K_RIGHT:
                to_right = True
            if event.key == pygame.K_UP:
                up = True
            if event.key == pygame.K_DOWN:
                down = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                to_left = False
            if event.key == pygame.K_RIGHT:
                to_right = False
            if event.key == pygame.K_UP:
                up = False
            if event.key == pygame.K_DOWN:
                down = False            

        if event.type == pygame.QUIT:
            exit()

    if to_right:
        x += 2
        if x > 640 - robot_width:
            x = 640 - robot_width
    if to_left:
        x -= 2
        if x < 0:
            x = 0
    if up:
        y -= 2
        if y < 0:
            y = 0
    if down:
        y += 2
        if y > 480 - robot_height:
            y = 480 - robot_height

    window.fill((0, 0, 0))
    window.blit(robot, (x, y))
    pygame.display.flip()

    clock.tick(60)