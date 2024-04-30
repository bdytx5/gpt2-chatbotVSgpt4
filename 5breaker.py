# make a python brick breaker (breakout) game make a python brick breaker (breakout) game make a python brick breaker (breakout) game make a python brick breaker (breakout) game make a python brick breaker (breakout) game make a python brick breaker (breakout) game make a python brick breaker (breakout) game make a python brick breaker (breakout) game make a python brick breaker (breakout) game make a python brick breaker (breakout) game make a python brick breaker (breakout) game make a python brick breaker (breakout) game make a python brick breaker (breakout) game make a python brick breaker (breakout) game make a python brick breaker (breakout) game make a python brick breaker (breakout) game make a python brick breaker (breakout) game make a python brick breaker (breakout) game make a python brick breaker (breakout) game make a python brick breaker (breakout) game 

import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
PADDLE_WIDTH, PADDLE_HEIGHT = 100, 20
BALL_RADIUS = 10
BRICK_WIDTH, BRICK_HEIGHT = 75, 30

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)

# Setup the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Brick Breaker")

# Paddle
paddle = pygame.Rect(SCREEN_WIDTH // 2 - PADDLE_WIDTH // 2, SCREEN_HEIGHT - 50, PADDLE_WIDTH, PADDLE_HEIGHT)

# Ball
ball = pygame.Rect(SCREEN_WIDTH // 2 - BALL_RADIUS, SCREEN_HEIGHT // 2 - BALL_RADIUS, BALL_RADIUS * 2, BALL_RADIUS * 2)
ball_dx, ball_dy = 5 * random.choice([-1, 1]), -5

# Bricks
bricks = []
for y in range(5):
    for x in range(SCREEN_WIDTH // BRICK_WIDTH):
        bricks.append(pygame.Rect(x * (BRICK_WIDTH + 10) + 15, y * (BRICK_HEIGHT + 5) + 15, BRICK_WIDTH, BRICK_HEIGHT))

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Paddle movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle.left > 0:
        paddle.left -= 5
    if keys[pygame.K_RIGHT] and paddle.right < SCREEN_WIDTH:
        paddle.right += 5

    # Ball movement
    ball.left += ball_dx
    ball.top += ball_dy

    # Ball collision with walls
    if ball.left <= 0 or ball.right >= SCREEN_WIDTH:
        ball_dx = -ball_dx
    if ball.top <= 0:
        ball_dy = -ball_dy
    if ball.bottom >= SCREEN_HEIGHT:
        running = False  # Game over

    # Ball collision with paddle
    if ball.colliderect(paddle):
        ball_dy = -ball_dy

    # Ball collision with bricks
    hit_index = ball.collidelist(bricks)
    if hit_index != -1:
        hit_rect = bricks.pop(hit_index)
        if abs(ball.centerx - hit_rect.centerx) > abs(ball.centery - hit_rect.centery):
            ball_dx = -ball_dx
        else:
            ball_dy = -ball_dy

    # Drawing everything
    screen.fill(BLACK)
    pygame.draw.rect(screen, BLUE, paddle)
    pygame.draw.circle(screen, WHITE, (ball.centerx, ball.centery), BALL_RADIUS)
    for brick in bricks:
        pygame.draw.rect(screen, RED, brick)

    pygame.display.flip()
    pygame.time.Clock().tick(60)

pygame.quit()