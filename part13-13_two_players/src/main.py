# WRITE YOUR SOLUTION HERE:
import pygame
import sys

pygame.init()
window = pygame.display.set_mode((640, 480))

robot1 = pygame.image.load("robot1.png")
robot2 = pygame.image.load("robot2.png")
robot1_width, robot1_height = robot1.get_size()
robot2_width, robot2_height = robot2.get_size()

x1, y1 = 0, 480 - robot1_height
x2, y2 = 640 - robot2_width, 480 - robot2_height

to_right1 = to_left1 = up1 = down1 = False
to_right2 = to_left2 = up2 = down2 = False

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            # Player 1 controls (arrow keys)
            if event.key == pygame.K_LEFT:
                to_left1 = True
            if event.key == pygame.K_RIGHT:
                to_right1 = True
            if event.key == pygame.K_UP:
                up1 = True
            if event.key == pygame.K_DOWN:
                down1 = True
            
            # Player 2 controls (W, A, S, D keys)
            if event.key == pygame.K_a:
                to_left2 = True
            if event.key == pygame.K_d:
                to_right2 = True
            if event.key == pygame.K_w:
                up2 = True
            if event.key == pygame.K_s:
                down2 = True

        if event.type == pygame.KEYUP:
            # Player 1 controls
            if event.key == pygame.K_LEFT:
                to_left1 = False
            if event.key == pygame.K_RIGHT:
                to_right1 = False
            if event.key == pygame.K_UP:
                up1 = False
            if event.key == pygame.K_DOWN:
                down1 = False
            
            # Player 2 controls
            if event.key == pygame.K_a:
                to_left2 = False
            if event.key == pygame.K_d:
                to_right2 = False
            if event.key == pygame.K_w:
                up2 = False
            if event.key == pygame.K_s:
                down2 = False

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Player 1 movement
    if to_right1:
        x1 += 2
        if x1 > 640 - robot1_width:
            x1 = 640 - robot1_width
    if to_left1:
        x1 -= 2
        if x1 < 0:
            x1 = 0
    if up1:
        y1 -= 2
        if y1 < 0:
            y1 = 0
    if down1:
        y1 += 2
        if y1 > 480 - robot1_height:
            y1 = 480 - robot1_height

    # Player 2 movement
    if to_right2:
        x2 += 2
        if x2 > 640 - robot2_width:
            x2 = 640 - robot2_width
    if to_left2:
        x2 -= 2
        if x2 < 0:
            x2 = 0
    if up2:
        y2 -= 2
        if y2 < 0:
            y2 = 0
    if down2:
        y2 += 2
        if y2 > 480 - robot2_height:
            y2 = 480 - robot2_height

    window.fill((0, 0, 0))
    window.blit(robot1, (x1, y1))
    window.blit(robot2, (x2, y2))
    pygame.display.flip()

    clock.tick(60)
