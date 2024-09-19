# Complete your game here
import pygame
import random
import sys

pygame.init()

# Constants
WINDOW_WIDTH, WINDOW_HEIGHT = 640, 480
PLAYER_SIZE = 50
ENEMY_SIZE = 50
COIN_SIZE = 30
TIME_LIMIT = 30  # in seconds

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Load images
robot = pygame.image.load("robot.png")
coin = pygame.image.load("coin.png")
monster = pygame.image.load("monster.png")
door = pygame.image.load("door.png")

# Scale images to desired sizes
robot = pygame.transform.scale(robot, (PLAYER_SIZE, PLAYER_SIZE))
coin = pygame.transform.scale(coin, (COIN_SIZE, COIN_SIZE))
monster = pygame.transform.scale(monster, (ENEMY_SIZE, ENEMY_SIZE))
door = pygame.transform.scale(door, (PLAYER_SIZE, PLAYER_SIZE))

# Initialize screen
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Coin Collector")

# Initialize game variables
player_x = WINDOW_WIDTH // 2
player_y = WINDOW_HEIGHT // 2
player_speed = 5

coins = [(random.randint(0, WINDOW_WIDTH - COIN_SIZE), random.randint(0, WINDOW_HEIGHT - COIN_SIZE)) for _ in range(5)]
monsters = [(random.randint(0, WINDOW_WIDTH - ENEMY_SIZE), random.randint(0, WINDOW_HEIGHT - ENEMY_SIZE)) for _ in range(3)]

score = 0
start_time = pygame.time.get_ticks()

font = pygame.font.Font(None, 36)

def draw_window():
    window.fill(BLACK)
    window.blit(robot, (player_x, player_y))
    
    for cx, cy in coins:
        window.blit(coin, (cx, cy))
    
    for mx, my in monsters:
        window.blit(monster, (mx, my))
    
    # Draw the score and time remaining
    score_text = font.render(f"Score: {score}", True, WHITE)
    window.blit(score_text, (10, 10))
    
    elapsed_time = (pygame.time.get_ticks() - start_time) / 1000
    time_remaining = max(0, TIME_LIMIT - int(elapsed_time))
    time_text = font.render(f"Time: {time_remaining}s", True, WHITE)
    window.blit(time_text, (10, 50))
    
    pygame.display.flip()

def move_player(keys):
    global player_x, player_y
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed
    if keys[pygame.K_UP]:
        player_y -= player_speed
    if keys[pygame.K_DOWN]:
        player_y += player_speed
    
    # Ensure player stays within window boundaries
    player_x = max(0, min(player_x, WINDOW_WIDTH - PLAYER_SIZE))
    player_y = max(0, min(player_y, WINDOW_HEIGHT - PLAYER_SIZE))

def check_collisions():
    global score
    global coins
    global monsters

    # Check for coin collisions
    coins_to_remove = []
    for i, (cx, cy) in enumerate(coins):
        if player_x < cx + COIN_SIZE and player_x + PLAYER_SIZE > cx and player_y < cy + COIN_SIZE and player_y + PLAYER_SIZE > cy:
            coins_to_remove.append(i)
            score += 1
    
    # Remove collected coins
    for i in reversed(coins_to_remove):
        coins.pop(i)

    # Check for monster collisions
    for mx, my in monsters:
        if player_x < mx + ENEMY_SIZE and player_x + PLAYER_SIZE > mx and player_y < my + ENEMY_SIZE and player_y + PLAYER_SIZE > my:
            pygame.quit()
            sys.exit()

def main():
    global start_time
    clock = pygame.time.Clock()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        move_player(keys)
        check_collisions()
        
        draw_window()
        
        elapsed_time = (pygame.time.get_ticks() - start_time) / 1000
        if elapsed_time >= TIME_LIMIT:
            pygame.quit()
            sys.exit()
        
        clock.tick(30)

if __name__ == "__main__":
    main()
