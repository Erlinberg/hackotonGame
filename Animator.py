import pygame

class Animation():
    def __init__(self, animCount, rootObject):
        self.animCount = animCount
        self.rootObject = rootObject

        self.currentAnimFrame = 0
        self.currentGameFrame = 0

        self.speedGlobal = 1

    def animateOnce(self, images, speedLocal):
        if self.currentGameFrame == 61:
            self.currentGameFrame = 0
        if self.currentGameFrame % (60 // (self.animCount*self.speedGlobal*speedLocal)) == 0 and self.currentGameFrame != 0:
            self.currentAnimFrame+=1

        if self.currentAnimFrame == self.animCount:
            self.currentAnimFrame = 0
            return True

        self.rootObject.image = images[self.currentAnimFrame]

        self.currentGameFrame += 1

        return False
    
    def animateRepeat(self, images, speedLocal):
        if self.currentGameFrame == 61:
            self.currentGameFrame = 0
        if self.currentGameFrame % (60 // (self.animCount*self.speedGlobal*speedLocal)) == 0 and self.currentGameFrame != 0:
            self.currentAnimFrame+=1

        if self.currentAnimFrame == self.animCount:
            self.currentAnimFrame = 0

        self.rootObject.image = images[self.currentAnimFrame]

        self.currentGameFrame += 1
