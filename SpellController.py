import pygame

def Diff(li1, li2):
    li_dif = [i for i in li1 + li2 if i not in li1 or i not in li2]
    return li_dif

class Dot(pygame.sprite.Sprite):
    def __init__(self, dotID):
        super(Dot, self).__init__()
        self.active = False

        self.image = pygame.Surface((20, 20))
        self.image.fill((255,0,0))
        
        self.rect = self.image.get_rect()

        self.yID, self.ID = dotID

    def set_position(self, centerDotPos, offset):
        self.rect.y = centerDotPos.y + (self.yID%3-1)*(self.rect.width + offset)
        self.rect.x = centerDotPos.x + (self.ID%3-1)*(self.rect.height + offset)

        

class SpellController():
    def __init__(self, mouseController):
        self.dots = [
            [Dot((0,0)),Dot((0,1)),Dot((0,2))],
            [Dot((1,3)),Dot((1,4)),Dot((1,5))],
            [Dot((2,6)),Dot((2,7)),Dot((2,8))]
            ]

        self.activeDots = []
        self.dotsGroup = pygame.sprite.Group([j for sub in self.dots for j in sub])

        self.spells = {(4,2):"basicSpell"}


        self.mouseController = mouseController

    @property
    def centerDot(self):
        return self.dots[1][1]
    
    def spellSquareActivation(self, mousePos):
        self.activeDots.append(self.centerDot)
        self.centerDot.rect.center = (mousePos[0],mousePos[1])
        self.centerDot.active = True
        for line in self.dots:
            for dot in line:
                dot.set_position(self.centerDot.rect,20)

    def drawConnections(self,renderer):
            startPos = self.activeDots[0].rect.center
            for dot in self.activeDots[1:]:
                renderer.drawLine(startPos,(dot.rect.center),(213,70,25),11)
                startPos = dot.rect.center

    def spellSquareUpdate(self,renderer):
        self.drawConnections(renderer)
        for line in self.dots:
            for dot in line:
                renderer.blitUI(dot)

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
            print(order)
            spell = self.recursionFindSpell(order)
            for dot in self.activeDots:
                dot.active = False
            self.activeDots.clear()

    def drawSpellSquare(self, renderer):
        if self.activeDots:
            self.spellSquareUpdate(renderer)

    def recursionFindSpell(self,key):
        if not len(key) == 1:
            if tuple(key) in self.spells:
                self.castSpell(self.spells[tuple(key)])
            else:
                self.recursionFindSpell(key[:-1])

    def castSpell(self, spell):
            print(spell)

                

