import pygame

pygame.init()

class Display:
    def __init__(self, width, height, title):
        self.width = width
        self.height = height
        self.title = title

    def window(self):
        screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(self.title)

        return screen
        
        
        
