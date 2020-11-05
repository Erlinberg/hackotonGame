import pygame
from Animator import Animation

class Player(pygame.sprite.Sprite):
    def __init__(self,screen, images, ends): # ends: idle, walk_down, walk_up
        super(Player, self).__init__()
        self.images = []
        self.ends = ends
        self.currentState = ends[0]
        
        for image in images:
            self.images.append(pygame.transform.scale(image, (40,40)))

        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.rect.center = (screen[0]//2,screen[1]//2)

        self.animationController = Animation(self.currentState[1],self)

    def update(self):
        self.animationController.animate(self.images[self.currentState[0]:self.currentState[1]])