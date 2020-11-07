import pygame
from Animator import Animation

class Spell(pygame.sprite.Sprite):
    def __init__(self,imageSet,radius,damage, enemyGroup, renderer, centerPos):
        super(Spell, self).__init__()
        self.images = imageSet
        self.image = self.images[0]
        self.rect = self.image.get_rect()

        self.rect.centerx, self.rect.centery = centerPos[0]//2+renderer.cameraOffset[0],centerPos[1]//2+renderer.cameraOffset[1]

        self.animationController = Animation(len(imageSet),self)

        self.damage = damage
        self.radius = pygame.Rect(self.rect.center, (radius*2, radius*2))

        self.intersects(enemyGroup)

    def intersects(self,enemyGroup):
        for sprite in enemyGroup:
            if self.radius.colliderect(sprite.rect):
                sprite.dealDamage(damage)
    
    def update(self):
        if self.animationController.animateOnce(self.images, 3):
            self.kill()
        
