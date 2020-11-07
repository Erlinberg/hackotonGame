import pygame
from Animator import Animation

class Player(pygame.sprite.Sprite):
    def __init__(self,screen, images, ends): # ends: idle, walk_down, walk_right, walk_left,,walk_up, spell
        super(Player, self).__init__()
        self.images = []
        self.ends = ends
        self.currentState = ends[0]
        
        for image in images:
            self.images.append(pygame.transform.scale(image, (40,40)))

        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.rect.center = (screen[0]//2,screen[1]//2)

        self.spellCasting = False
        self.animationController = Animation(self.currentState[1],self)

        self.lives = 100

    @property
    def currentAnimation(self):
        return self.ends.index(self.currentState)

    def dealDamage(self,damage):
        self.lives -= damage

    def changeAnimation(self,id):
        self.currentState = self.ends[id]
        self.animationController.animCount = self.currentState[1]-self.currentState[0]
        self.animationController.currentAnimFrame = 0
        self.animationController.currentGameFrame = 0

    def castingSpell(self,animID=5):
        self.spellCasting = True
        self.changeAnimation(animID)

    def update(self):
        if not self.spellCasting:
            self.animationController.animateRepeat(self.images[self.currentState[0]:self.currentState[1]],2)
        else:
            if self.animationController.animateOnce(self.images[self.currentState[0]:self.currentState[1]],1.8):
                self.spellCasting = False
                self.changeAnimation(0)