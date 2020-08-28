import pygame
from random import randint
from Display import Dis

pygame.init()

Display = Dis()


def main():
    # player
    player_y = 550 - 16
    player_x = 300
    player_x_change = 0
    player_height = 15
    player_width = 100

    # ball
    ball_x = randint(50, (550 - 50 - 25))
    ball_y = randint(50, 100)
    ball_x_change = -1.5
    ball_y_change = 1.5
    ball_height = 25
    ball_width = 25

    # Score

    score_value = 0
    font = pygame.font.SysFont("comicsansms", 65)

    score_textX = 10
    score_textY = 10

    collision_can_happen = True

    # functions
    def player(x, y):
        pygame.draw.rect(window, (0, 0, 0), [
                         x, y, player_width, player_height])

    def ball(x, y):
        pygame.draw.rect(window, (0, 0, 0), [x, y, ball_width, ball_height])

    def isCollision(player_height, player_width, player_x, player_y, ball_height, ball_width, ball_x, ball_y):
        if player_x < ball_x + ball_width and player_x + player_width > ball_x and player_y < ball_y + ball_height and player_y + player_height > ball_y:
            return True
        else:
            return False

    def show_score(x, y):
        score = font.render("Score : " + str(score_value), True, (0, 0, 0))
        window.blit(score, (x, y))

    window = Display.win(height=550, width=700, title="Game")
    run = True

    while run:

        pygame.time.delay(1)
        window.fill((255, 255, 255))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    player_x_change = 1.5

                if event.key == pygame.K_LEFT:
                    player_x_change = -1.5

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    player_x_change = 0

        player_x += player_x_change
        if player_x <= 0:
            player_x = 0
        elif player_x >= 600:
            player_x = 600

        ball_x += ball_x_change
        ball_y += ball_y_change

        if ball_x <= 0:
            ball_x = 0
            ball_x_change *= -1

        if ball_y <= 0:
            ball_y = 0
            ball_y_change *= -1

        if ball_y >= 550 - 25:
            ball_y = 550 - 25
            ball_y_change *= -1

        if ball_x >= 700 - 25:
            ball_x = 700 - 25
            ball_x_change *= -1

        collison = isCollision(player_height=player_height, player_width=player_width, player_x=player_x,
                               player_y=player_y, ball_height=ball_height, ball_width=ball_width, ball_x=ball_x,
                               ball_y=ball_y)
        if collision_can_happen:
            if collison:
                ball_y_change *= -1

                score_value += 1

        player(player_x, player_y)
        ball(ball_x, ball_y)
        show_score(score_textX, score_textY)
        pygame.display.flip()


main()
