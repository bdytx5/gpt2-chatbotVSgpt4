import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Brick Breaker")

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
orange = (255, 165, 0)

# Fonts
font = pygame.font.Font(None, 36)

# Ball setup
ball_x = width // 2
ball_y = height // 2
ball_dx = 3 * random.choice([-1, 1])
ball_dy = -3
ball_size = 10

# Paddle setup
paddle_width = 100
paddle_height = 20
paddle_x = (width - paddle_width) // 2
paddle_y = height - paddle_height - 10

# Brick setup
brick_rows = 5
brick_cols = 7
brick_width = 100
brick_height = 30
brick_padding = 10
bricks = []

# Score
score = 0

# Create bricks
for i in range(brick_rows):
    for j in range(brick_cols):
        brick_x = j * (brick_width + brick_padding) + 30
        brick_y = i * (brick_height + brick_padding) + 30
        bricks.append(pygame.Rect(brick_x, brick_y, brick_width, brick_height))

# Particles for the fire effect
particles = []

clock = pygame.time.Clock()
running = True

# Function to add particles
def add_particles(position):
    particle_count = 10
    for _ in range(particle_count):
        particles.append([list(position), [random.randint(0, 20) / 10 - 1, -2], random.randint(4,6)])

# Game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Movement controls
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle_x > 0:
        paddle_x -= 5
    if keys[pygame.K_RIGHT] and paddle_x < width - paddle_width:
        paddle_x += 5

    # Ball movement
    ball_x += ball_dx
    ball_y += ball_dy

    # Add fire particles
    add_particles([ball_x, ball_y + ball_size])

    # Ball collision with walls
    if ball_x <= 0 or ball_x >= width:
        ball_dx = -ball_dx
    if ball_y <= 0:
        ball_dy = -ball_dy
    if ball_y >= height:
        running = False  # Game over

    # Ball collision with paddle
    if paddle_x < ball_x < paddle_x + paddle_width and paddle_y < ball_y < paddle_y + paddle_height:
        ball_dy = -ball_dy

    # Ball collision with bricks
    for brick in bricks[:]:
        if brick.collidepoint(ball_x, ball_y):
            bricks.remove(brick)
            ball_dy = -ball_dy
            score += 100  # Increment score
            break

    # Update and draw particles
    for particle in particles[:]:
        particle[0][0] += particle[1][0]
        particle[0][1] += particle[1][1]
        particle[2] -= 0.1  # Shrink particle
        if particle[2] <= 0:
            particles.remove(particle)

    # Drawing
    screen.fill(black)
    pygame.draw.rect(screen, blue, (paddle_x, paddle_y, paddle_width, paddle_height))
    pygame.draw.circle(screen, white, (ball_x, ball_y), ball_size)
    for brick in bricks:
        pygame.draw.rect(screen, red, brick)
    for particle in particles:
        pygame.draw.circle(screen, orange, [int(particle[0][0]), int(particle[0][1])], int(particle[2]))

    # Draw score
    score_text = font.render(f"Score: {score}", True, yellow)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
