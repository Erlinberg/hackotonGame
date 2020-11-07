import pygame


# NOT DONE
# NOT SURE IF WE NEED THIS
#
#
#
class Particle(pygame.sprite.Sprite):
    def __init__(self,image,pos,direction):
        self.image = image
        self.rect = image.get_rect()
        self.rect.position = pos

        self.direction = direction # degree -> 0 is right

    def update(self):
        self.rect.move_ip()

class VisualEffects():
    def __init__(self):
