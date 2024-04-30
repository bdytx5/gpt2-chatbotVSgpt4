import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
PADDLE_WIDTH, PADDLE_HEIGHT = 100, 20
BALL_RADIUS = 10
BRICK_WIDTH, BRICK_HEIGHT = 75, 30
FPS = 60

# Colors
WHITE = (255, 255, 255)
RED = (217, 87, 99)
BLUE = (69, 177, 232)
YELLOW = (251, 242, 54)
BLACK = (0, 0, 0)
ORANGE = (253, 164, 17)

# Fonts
font = pygame.font.Font(None, 36)

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

# Particles for the fire effect
particles = []

# Game loop
running = True
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Paddle movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle.left > 0:
        paddle.left -= 7
    if keys[pygame.K_RIGHT] and paddle.right < SCREEN_WIDTH:
        paddle.right += 7

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

    # Fire particles
    particles.append([[ball.centerx, ball.centery], [random.randint(0, 20) / 10 - 1, -2], random.randint(4, 6)])

    # Update particles
    for particle in particles[:]:
        particle[0][0] += particle[1][0]
        particle[0][1] += particle[1][1]
        particle[2] -= 0.2  # shrink the particle
        if particle[2] <= 0:
            particles.remove(particle)

    # Drawing everything
    screen.fill(BLACK)
    pygame.draw.rect(screen, BLUE, paddle)
    pygame.draw.circle(screen, YELLOW, (ball.centerx, ball.centery), BALL_RADIUS)
    for brick in bricks:
        pygame.draw.rect(screen, RED, brick)
    for particle in particles:
        pygame.draw.circle(screen, ORANGE, [int(particle[0][0]), int(particle[0][1])], int(particle[2]))
    # Display score
    score_text = font.render(f'Score: {50 - len(bricks)}', True, WHITE)  # Calculate score as total initial bricks minus remaining
    screen.blit(score_text, (10, 10))

    # Check for game over (when all bricks are gone)
    if not bricks:
        game_over_text = font.render("YOU WIN!", True, YELLOW)
        screen.blit(game_over_text, (SCREEN_WIDTH // 2 - game_over_text.get_width() // 2, SCREEN_HEIGHT // 2 - game_over_text.get_height() // 2))
        pygame.display.flip()  # Update the display
        pygame.time.wait(3000)  # Pause for 3 seconds
        running = False  # End the game loop

    pygame.display.flip()  # Update the display
    clock.tick(FPS)  # Maintain 60 frames per second

pygame.quit()