import pygame, random

# Initialize Pygame and constants
pygame.init()
SW, SH = 800, 600
screen = pygame.display.set_mode((SW, SH))
pygame.display.set_caption("Brick Breaker")
clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)

# Colors and settings
colors = {'white': (255, 255, 255), 'red': (217, 87, 99), 'blue': (69, 177, 232),
          'yellow': (251, 242, 54), 'black': (0, 0, 0), 'orange': (253, 164, 17)}
PW, PH, BR, BW, BH, FPS = 100, 20, 10, 75, 30, 60
ball_vel = [5 * random.choice([-1, 1]), -5]

# Game objects
paddle = pygame.Rect(SW//2 - PW//2, SH - 50, PW, PH)
ball = pygame.Rect(SW//2 - BR, SH//2 - BR, 2*BR, 2*BR)
bricks = [pygame.Rect(x * (BW + 10) + 15, y * (BH + 5) + 15, BW, BH) for y in range(5) for x in range(SW // BW)]
particles = []

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Input handling
    keys = pygame.key.get_pressed()
    paddle.left += (keys[pygame.K_RIGHT] and paddle.right < SW) * 7 - (keys[pygame.K_LEFT] and paddle.left > 0) * 7

    # Ball movement & wall collision
    ball.x += ball_vel[0]
    ball.y += ball_vel[1]
    ball_vel[0] *= (ball.left <= 0 or ball.right >= SW) * -2 + 1
    ball_vel[1] *= (ball.top <= 0 or ball.bottom >= SH) * -2 + 1
    if ball.bottom >= SH: running = False  # Game over

    # Ball collision with paddle
    if ball.colliderect(paddle):
        ball_vel[1] = -ball_vel[1]

    # Ball collision with bricks
    hit_index = ball.collidelist(bricks)
    if hit_index != -1:
        hit_rect = bricks.pop(hit_index)
        ball_vel[0] *= (abs(ball.centerx - hit_rect.centerx) > abs(ball.centery - hit_rect.centery)) * -2 + 1
        ball_vel[1] *= (abs(ball.centerx - hit_rect.centerx) <= abs(ball.centery - hit_rect.centery)) * -2 + 1

    # Fire particles
    particles.append([[ball.centerx, ball.centery], [random.randint(0, 20) / 10 - 1, -2], random.randint(4, 6)])
    particles = [[[p[0][0] + p[1][0], p[0][1] + p[1][1]], p[1], p[2] - 0.2] for p in particles if p[2] > 0]

    # Draw everything
    screen.fill(colors['black'])
    pygame.draw.rect(screen, colors['blue'], paddle)
    pygame.draw.circle(screen, colors['yellow'], (ball.centerx, ball.centery), BR)
    for brick in bricks:
        pygame.draw.rect(screen, colors['red'], brick)
    for p in particles:
        pygame.draw.circle(screen, colors['orange'], [int(p[0][0]), int(p[0][1])], int(p[2]))

    # Score & game over checks
    score_text = font.render(f'Score: {50 - len(bricks)}', True, colors['white'])
    screen.blit(score_text, (10, 10))
    if not bricks:
        game_over_text = font.render("YOU WIN!", True, colors['yellow'])
        screen.blit(game_over_text, (SW//2 - game_over_text.get_width()//2, SH//2 - game_over_text.get_height()//2))
        pygame.display.flip()
        pygame.time.wait(3000)
        running = False

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()