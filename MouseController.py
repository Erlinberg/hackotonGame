import pygame

class MouseController(pygame.sprite.Sprite):
    def __init__(self):
        self.image = pygame.Surface((1,1))
        self.rect = self.image.get_rect()

    @property
    def mousePos(self):
        return pygame.mouse.get_pos()

    @property
    def isLMBPressed(self):
        return pygame.mouse.get_pressed()[0]

    def update(self):
        self.rect.x, self.rect.y = self.mousePos