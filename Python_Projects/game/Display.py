import pygame

pygame.init()


class Dis:
    def win(self, width, title, height):
        win = pygame.display.set_mode((width, height))
        pygame.display.set_caption(title)
        return win
