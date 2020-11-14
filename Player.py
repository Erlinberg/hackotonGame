import pygame
from Animator import Animation

class Player(pygame.sprite.Sprite):
    def __init__(self,screen, images, ends): # ends: idle, walk_down, walk_right, walk_left,,walk_up, spell
        super(Player, self).__init__()
        self.images = images
        self.ends = ends
        self.currentState = ends[0]

        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.rect.center = (20*23,22*23 - 1)

        self.spellCasting = False
        self.currentSpell = None
        self.animationController = Animation(self.currentState[1],self)
        
        self.defaultHP = 100
        self.lives = 100

        self.defaultMana = 100
        self.mana = 100

        self.spellAnims = {
            "cutSpell":(5,1.8),
            "lightingSpell":(6,1),
            "explosionSpell":(6,1)
        }

        self.timerStart = 0

    def startTimer(self):
        self.timerStart = pygame.time.get_ticks()

    def timerUpdate(self):
        if not self.mana == self.defaultMana:
            seconds=(pygame.time.get_ticks()-self.timerStart)/1000 #calculate how many seconds
            if seconds > 4:
                self.mana += 1

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
        self.image = self.images[self.currentState[0]:self.currentState[1]][0]
        center = self.rect.center
        self.rect = pygame.Rect((self.rect.x,self.rect.y), self.image.get_size())
        self.rect.center = center

    def castingSpell(self,spellName,spell):
        self.spellCasting = spellName

        if self.currentSpell:
            self.currentSpell.activated = True

        self.currentSpell = spell
        self.mana -= self.currentSpell.manaConsuptions
        self.startTimer()
        self.changeAnimation(self.spellAnims[spellName][0])
    
    def freeze(self):
        pass

    def update(self):
        if not self.spellCasting:
            self.animationController.animateRepeat(self.images[self.currentState[0]:self.currentState[1]],2)
        else:
            if self.animationController.animateOnce(self.images[self.currentState[0]:self.currentState[1]],self.spellAnims[self.spellCasting][1]):
                self.spellCasting = ''
                self.currentSpell.activated = True
                self.changeAnimation(0)

        self.timerUpdate()