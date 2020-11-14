import pygame
from Animator import Animation

class Spell(pygame.sprite.Sprite):
    def __init__(self,imageSet,radius,damage, yOffset, mana, enemy, renderer, centerPos):
        super(Spell, self).__init__()
        self.images = imageSet
        self.image = self.images[0]
        self.rect = self.image.get_rect()

        self.rect.centerx, self.rect.centery = centerPos[0]//2+renderer.cameraOffset[0],centerPos[1]//2+renderer.cameraOffset[1]
        self.rect.y -= yOffset

        self.animationController = Animation(len(imageSet),self)

        self.damage = damage
        self.radius = pygame.Rect(self.rect.midbottom, (radius*2, radius*2))

        self.activated = False
        self.manaConsuptions = mana

        self.intersects(enemy)

    def intersects(self,enemy):
        if self.radius.colliderect(enemy.rect):
            enemy.dealDamage(self.damage)
            
    
    def update(self):
        if self.animationController.animateOnce(self.images, 2):
            self.kill()
        
