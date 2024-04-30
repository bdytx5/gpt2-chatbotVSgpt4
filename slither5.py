# prompt = write a python game similar to slither io 
import pygame
import sys
import random
import time
# Initialize Pygame
pygame.init()
# Constants for the game
SCREEN_WIDTH, SCREEN_HEIGHT = 600, 480
BACKGROUND_COLOR = (0, 0, 0)  # Black
SNAKE_COLOR = (0, 255, 0)     # Green
FOOD_COLOR = (255, 0, 0)      # Red
SNAKE_SIZE = 10  # Size of the snake
FOOD_SIZE = 10   # Size of the food
FPS = 15
# Create the screen object
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# Set title of the window
pygame.display.set_caption('Slither.io Clone')
# Clock to set FPS
clock = pygame.time.Clock()
# Snake initial position and segments
snake_pos = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50]]
# Food initial random position
food_pos = [random.randrange(1, (SCREEN_WIDTH//10)) * 10, random.randrange(1, (SCREEN_HEIGHT//10)) * 10]
food_spawn = True
# Direction control for snake (right initially)
dx, dy = 10, 0
# Whether the game is over
game_over = False
def check_collision(positions):
    # Check if the head collides with body
    head = positions[0]
    body = positions[1:]
    if head in body:
        return True
    return False
# Game loop
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # Event handling, changes the keystrokes received into directions
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                dx, dy = 0, -10
            elif event.key == pygame.K_DOWN:
                dx, dy = 0, 10
            elif event.key == pygame.K_LEFT:
                dx, dy = -10, 0
            elif event.key == pygame.K_RIGHT:
                dx, dy = 10, 0
    # Move the snake
    snake_pos[0] += dx
    snake_pos[1] += dy
    # Snake body growing mechanism
    snake_body.insert(0, list(snake_pos))
    if snake_pos == food_pos:
        food_spawn = False
    else:
        snake_body.pop()
    # Food Spawn
    if not food_spawn:
        food_pos = [random.randrange(1, (SCREEN_WIDTH//10)) * 10, random.randrange(1, (SCREEN_HEIGHT//10)) * 10]
    food_spawn = True
    # Game Over conditions
    if snake_pos[0] >= SCREEN_WIDTH or snake_pos[0] < 0 or snake_pos[1] >= SCREEN_HEIGHT or snake_pos[1] < 0:
        game_over = True
    if check_collision(snake_body):
        game_over = True
    # Fill the background and draw the snake and food
    screen.fill(BACKGROUND_COLOR)
    for pos in snake_body:
        pygame.draw.rect(screen, SNAKE_COLOR, pygame.Rect(pos[0], pos[1], SNAKE_SIZE, SNAKE_SIZE))
    pygame.draw.rect(screen, FOOD_COLOR, pygame.Rect(food_pos[0], food_pos[1], FOOD_SIZE, FOOD_SIZE))
    # Update the full display
    pygame.display.flip()
    # Set the speed of the game
    clock.tick(FPS)
# If game over show a message
if game_over:
    font = pygame.font.SysFont('arial', 48)
    game_over_surface = font.render('Game Over', True, (255, 255, 255))
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (SCREEN_WIDTH/2, SCREEN_HEIGHT/4)
    screen.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
    time.sleep(3)
    pygame.quit()
    sys.exit()


