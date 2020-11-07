import pygame
from Animator import Animation

class SnowBoss(pygame.sprite.Sprite): #make class containing our boses
    def __init__(self,pos,images, ends): #taking in positions x and y; name of our image and amount of lives
        self.images = images
        self.ends = ends
        self.currentState = ends[0]

        self.rect = pygame.Rect((pos), self.image.get_size()) #make rectangle for the image
        self.lives = lives #amount of lives

        self.animationController = Animation(self.currentState[1],self)

    def dealDamage(damage):
        self.lives -= damage
        if self.live <= 0:
            self.death()
        else:
            pass
            #self.changeAnimation(id)


    def death(self): #death of the boss
        if self.live == 0: #if amount of lives reaches 0
            #self.changeAnimation(id)
            self.kill() #the boss dies


    def changeAnimation(self,id):
        self.currentState = self.ends[id]
        self.animationController.animCount = self.currentState[1]-self.currentState[0]
        self.animationController.currentAnimFrame = 0
        self.animationController.currentGameFrame = 0