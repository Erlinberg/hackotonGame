import pygame

class Animation():
    def __init__(self, animCount, rootObject):
        self.animCount = animCount
        self.rootObject = rootObject

        self.currentAnimFrame = 0
        self.currentGameFrame = 0

        self.speed = 2

    
    def animate(self, images):
        if self.currentGameFrame == 61:
            self.currentGameFrame = 0
        if self.currentGameFrame % (60 // (self.animCount*self.speed)) == 0 and self.currentGameFrame != 0:
            self.currentAnimFrame+=1

        if self.currentAnimFrame == self.animCount:
            self.currentAnimFrame = 0

        self.rootObject.image = images[self.currentAnimFrame]

        self.currentGameFrame += 1
