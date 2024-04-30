import pygame, random

# Initialize Pygame and constants
pygame.init()
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Brick Breaker")
FPS, BALL_RADIUS = 60, 10
colors = {'white': (255, 255, 255), 'red': (217, 87, 99), 'blue': (69, 177, 232), 'yellow': (251, 242, 54), 'black': (0, 0, 0), 'orange': (253, 164, 17)}
font = pygame.font.Font(None, 36)

# Paddle, ball, bricks setup
paddle = pygame.Rect(SCREEN_WIDTH // 2 - 50, SCREEN_HEIGHT - 50, 100, 20)
ball = pygame.Rect(SCREEN_WIDTH // 2 - BALL_RADIUS, SCREEN_HEIGHT // 2 - BALL_RADIUS, BALL_RADIUS * 2, BALL_RADIUS * 2)
ball_vel = [5 * random.choice([-1, 1]), -5]
bricks = [pygame.Rect(x * 85 + 15, y * 35 + 15, 75, 30) for y in range(5) for x in range(SCREEN_WIDTH // 75)]

# Game loop
running = True
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    paddle.x += (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * 7
    paddle.x = max(min(paddle.x, SCREEN_WIDTH - paddle.width), 0)
    ball.x += ball_vel[0]
    ball.y += ball_vel[1]
    if ball.left <= 0 or ball.right >= SCREEN_WIDTH:
        ball_vel[0] *= -1
    if ball.top <= 0 or ball.colliderect(paddle):
        ball_vel[1] *= -1
    if ball.bottom >= SCREEN_HEIGHT:
        running = False

    hit_index = ball.collidelist(bricks)
    if hit_index >= 0:
        brick = bricks.pop(hit_index)
        axis = (abs(ball.centerx - brick.centerx) > abs(ball.centery - brick.centery))
        ball_vel[axis] *= -1

    screen.fill(colors['black'])
    pygame.draw.rect(screen, colors['blue'], paddle)
    pygame.draw.circle(screen, colors['yellow'], (ball.centerx, ball.centery), BALL_RADIUS)
    for brick in bricks:
        pygame.draw.rect(screen, colors['red'], brick)
    score_text = font.render(f'Score: {50 - len(bricks)}', True, colors['white'])
    screen.blit(score_text, (10, 10))
    if not bricks:
        game_over_text = font.render("YOU WIN!", True, colors['yellow'])
        screen.blit(game_over_text, (SCREEN_WIDTH // 2 - game_over_text.get_width() // 2, SCREEN_HEIGHT // 2 - game_over_text.get_height() // 2))
        pygame.display.flip()
        pygame.time.wait(3000)
        running = False

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
