import pygame
from Spell import Spell

def Diff(li1, li2):
    li_dif = [i for i in li1 + li2 if i not in li1 or i not in li2]
    return li_dif

class SpellSquareEffect(pygame.sprite.Sprite):
    def __init__(self, center, size, border,rotationAngle, color):
        super(SpellSquareEffect, self).__init__()
        self.surface = self.createBorder(size,size,border,color)
        self.surfaceRect = self.surface.get_rect()
        self.surfaceRect.center = center
        
        self.image, self.rect = self.rotate(rotationAngle)

        self.currentAngle = rotationAngle

    def createBorder(self,width, height, border, border_color):
        surf = pygame.Surface((width+border*2, height+border*2), pygame.SRCALPHA)
        for i in range(1, border):
            pygame.draw.rect(surf, border_color, (border-i, border-i, width+5, height+5), 1)
        return surf

    def rotate(self, angle):
        center = self.surfaceRect.center
        rotated_image = pygame.transform.rotate(self.surface, angle)
        new_rect = rotated_image.get_rect(center = center)

        return rotated_image, new_rect

    def update(self):
        self.currentAngle -= 3
        self.image, self.rect = self.rotate(self.currentAngle%360)




class Dot(pygame.sprite.Sprite):
    def __init__(self, dotID, image):
        super(Dot, self).__init__()
        self.active = False

        self.image = image
        
        self.rect = self.image.get_rect()

        self.yID, self.ID = dotID

    def set_position(self, centerDotPos, offset):
        self.rect.y = centerDotPos.y + (self.yID%3-1)*(self.rect.width + offset)
        self.rect.x = centerDotPos.x + (self.ID%3-1)*(self.rect.height + offset)

        

class SpellController():
    def __init__(self, mouseController, imageStorage, renderer, player, soundController):
        self.dots = [
            [Dot((0,0),imageStorage["spellSquare"][0]),Dot((0,1),imageStorage["spellSquare"][0]),Dot((0,2),imageStorage["spellSquare"][0])],
            [Dot((1,3),imageStorage["spellSquare"][0]),Dot((1,4),imageStorage["spellSquare"][0]),Dot((1,5),imageStorage["spellSquare"][0])],
            [Dot((2,6),imageStorage["spellSquare"][0]),Dot((2,7),imageStorage["spellSquare"][0]),Dot((2,8),imageStorage["spellSquare"][0])]
            ]

        self.activeDots = []
        self.dotsGroup = pygame.sprite.Group([j for sub in self.dots for j in sub])

        self.spellsCode = {
            (4,0):"cutSpell",
            (4,1):"cutSpell",
            (4,2):"cutSpell",
            (4,3):"cutSpell",
            (4,5):"cutSpell",
            (4,6):"cutSpell",
            (4,7):"cutSpell",
            (4,8):"cutSpell",
            (4,7,8,5,2,1,0,3,6):"lightingSpell",
            (4,7,8):"explosionSpell"
        }

        self.spells = { #(image,range,damage,yOffset)
            "cutSpell":(imageStorage["cutSpell"],8,5,0,10),
            "lightingSpell":(imageStorage["lightingSpell"],2,50,130,40),
            "explosionSpell":(imageStorage["beamSpell"],20,25,75,30)
            } 

        self.spellGroup = pygame.sprite.Group()
        self.effects = pygame.sprite.Group([SpellSquareEffect((0,0), 196, 5,45,(83,168,57)),SpellSquareEffect((0,0), 100, 3,0,(237,5,5))])
        
        self.enemy = None
        self.player = player
        self.renderer = renderer
        self.mouseController = mouseController
        self.soundController = soundController

    @property
    def centerDot(self):
        return self.dots[1][1]

    @property
    def spellSquareActive(self):
        return len(self.activeDots) > 0
    
    def spellSquareActivation(self, mousePos):
        self.activeDots.append(self.centerDot)
        self.centerDot.rect.center = (mousePos[0],mousePos[1])
        self.centerDot.active = True
        for line in self.dots:
            for dot in line:
                dot.set_position(self.centerDot.rect,20)
        for effect in self.effects:
            effect.surfaceRect.center = self.centerDot.rect.center

    def drawConnections(self):
            startPos = self.activeDots[0].rect.center
            for dot in self.activeDots[1:]:
                self.renderer.drawLine(startPos,(dot.rect.center),(83,168,57),6)
                startPos = dot.rect.center

    def spellSquareUpdate(self):
        self.drawConnections()
        for effect in self.effects:
            self.renderer.blitUI(effect)
        for line in self.dots:
            for dot in line:
                self.renderer.blitUI(dot)
        

    def checkOnMouseClick(self,event):
        if self.mouseController.isLMBPressed:
            if not self.activeDots:
                self.spellSquareActivation(self.mouseController.mousePos)
            else:
                collidedDots = pygame.sprite.spritecollide(self.mouseController, self.dotsGroup, False)
                if collidedDots:
                    collidedDot = collidedDots[0]
                    if not collidedDot.active:
                        collidedDot.active = True
                        self.activeDots.append(collidedDot)
        elif event == pygame.MOUSEBUTTONUP:
            order = [dot.ID for dot in self.activeDots]
            spell = self.recursionFindSpell(order)
            for dot in self.activeDots:
                dot.active = False
            self.activeDots.clear()

    def drawSpellSquare(self):
        if self.activeDots:
            self.spellSquareUpdate()
            self.effects.update()

    def recursionFindSpell(self,key):
        if not len(key) <= 1:
            if tuple(key) in self.spellsCode:
                self.castSpell(self.spellsCode[tuple(key)])
            else:
                self.recursionFindSpell(key[:-1])

    def castSpell(self, spellName):
        if not self.player.mana - self.spells[spellName][-1] < 0:
            self.soundController.playSFXOnce(spellName)
            newSpell = Spell(*self.spells[spellName],self.enemy,self.renderer,self.centerDot.rect.center)
            self.player.castingSpell(spellName, newSpell)
            self.spellGroup.add(newSpell)

    def updateSpells(self):
        for spell in self.spellGroup:
            if spell.activated:
                spell.update()
            
    def blitSpells(self):
        for spell in self.spellGroup:
            if spell.activated:
                self.renderer.blitSprite(spell)

                

