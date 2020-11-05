import pygame
from PIL import Image

class Block(pygame.sprite.Sprite):
    def __init__(self,image,coords, group, offset, block_size):
        super(Block, self).__init__()

        self.image = image
        self.rect = pygame.Rect((offset[0]+coords[0]*block_size[0], offset[1]+coords[1]*block_size[1]), (block_size[0],block_size[1]))

        group.add(self)

class Decoration(pygame.sprite.Sprite):
    def __init__(self,image,coords, group, offset, block_size):
        super(Decoration, self).__init__()

        self.image = image
        self.rect = pygame.Rect((offset[0]+coords[0]*block_size[0], offset[1]+coords[1]*block_size[1]), (block_size[0],block_size[1]))

        group.add(self)
        
class Level():
    def __init__(self,level, decorations,levelName,imageSetLevel,imageSetDecoration,offset,block_size):
        self.level = level # [[]]
        self.decorations = decorations # [[]]
        self.levelName = levelName
        self.imageSetLevel = imageSetLevel #0: фон 1: стена 2: пол

        self.imageSetDecoration = imageSetDecoration #0: фон 1: стена 2: пол
        
        self.levelBlocks = pygame.sprite.Group()
        self.walls = pygame.sprite.Group()

        self.decorationsGroup = pygame.sprite.Group()


        self.buildLevel(offset, block_size)
        self.buildDecoration(offset, block_size)

    
        

    def buildLevel(self, offset, block_size):
        x,y = 0,0
        for row in self.level:
            for element in row:
                img = self.imageSetLevel[element]
                block = Block(img,(x,y),self.levelBlocks, offset, block_size)
        
                if element == 1:
                    self.walls.add(block)
                x += 1
            x,y = 0,y+1

    def buildDecoration(self, offset, block_size):
        x,y = 0,0
        for row in self.decorations:
            for element in row:
                img = self.imageSetDecoration[element]
                if element:
                    decoration = Decoration(img,(x,y),self.decorationsGroup, offset, block_size)
                x += 1
            x,y = 0,y+1

