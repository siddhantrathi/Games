import pygame
import sys
import time
from pygame import mixer




# functions



def opponent_animation():
    global opponent_speed

    opponent.y += opponent_speed
    if opponent.y >= height - 160:
        opponent_speed = 0
    if opponent.y <= 0:
        opponent_speed = 0




def player_animation():
    global player_speed

    player.y += player_speed
    if player.y >= height - 160:
        player_speed = 0
    if player.y <= 0:
        player_speed = 0

def ball_animation():
    global ball_speed_x, ball_speed_y, score, lives

    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.y >= height - 15 or ball.y <= 0:
        ball_speed_y *= -1

    if ball.x >= width - 15 or ball.x <= 0:
        ball_speed_x *= -1
        lives -= 1

    if ball.colliderect(player) and ball_speed_x > 0:
        if abs(ball.right - player.left) < 24:
            ball_speed_x *= -1
            score += 1

    if ball.colliderect(opponent) and ball_speed_x < 0:
        if abs(ball.left - opponent.right) < 24:
            ball_speed_x *= -1
            score += 1



# General Setup
width = 1200
height = 700

pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Pong')
clock = pygame.time.Clock()

# Game Rectangles

ball = pygame.Rect(width / 2 - 15, height / 2 - 15, 30, 30)
player = pygame.Rect(width - 28, height / 2 - 80, 24, 160)
opponent = pygame.Rect(24 - 20, height / 2 - 80, 24, 160)

# Score
score = 0
lives = 5



# player
player_speed = 0

# ball
ball_speed_x = 1
ball_speed_y = 1

# opponent
opponent_speed = 0


# Main Game_loop
while True:
    font = pygame.font.SysFont('monospace', 32, bold=True)
    dis_font = font.render(f'Score: {score}', 1, (64, 64, 64))
    dis_live = font.render(f'Lives: {lives}', 1, (64, 64, 64))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player_speed = -1

            if event.key == pygame.K_DOWN:
                player_speed = 1

            if event.key == pygame.K_w:
                opponent_speed = -1

            if event.key == pygame.K_s:
                opponent_speed = 1

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                player_speed = 0
            if event.key == pygame.K_w or event.key == pygame.K_s:
                opponent_speed = 0

    if lives <= 0:
        pygame.quit()
        sys.exit()



    player_animation()
    ball_animation()
    opponent_animation()



    # Visuals
    screen.fill((184, 178, 178))
    pygame.draw.ellipse(screen, (64, 64, 64), ball)
    pygame.draw.rect(screen, (64, 64, 64), player)
    pygame.draw.rect(screen, (64, 64, 64), opponent)
    screen.blit(dis_font, (4, 25))
    screen.blit(dis_live, (300, 25))
    # Updating The display
    pygame.display.flip()
    clock.tick(700 * 2 * 4)
