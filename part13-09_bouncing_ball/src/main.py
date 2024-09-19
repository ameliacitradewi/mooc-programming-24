# WRITE YOUR SOLUTION HERE:
import pygame
import math

pygame.init()
window = pygame.display.set_mode((640, 480))

ball = pygame.image.load("ball.png")
ball_rect = ball_image.get_rect()
ball_rect.center = (WIDTH // 2, HEIGHT // 2)
ball_speed_x = 5
ball_speed_y = 5

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Update ball position
    ball_rect.x += ball_speed_x
    ball_rect.y += ball_speed_y

    # Bounce off the edges
    if ball_rect.left < 0 or ball_rect.right > WIDTH:
        ball_speed_x = -ball_speed_x
    if ball_rect.top < 0 or ball_rect.bottom > HEIGHT:
        ball_speed_y = -ball_speed_y

    window.fill((0, 0, 0))
    window.blit(ball_image, ball_rect)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)
