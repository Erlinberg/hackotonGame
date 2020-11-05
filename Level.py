import pygame
from PIL import Image

class Block(pygame.sprite.Sprite):
    def __init__(self,image,coords, group, offset, block_size, number):
        super(Block, self).__init__()

        self.image = image
        self.rect = pygame.Rect((offset[0]+coords[0]*block_size[0], offset[1]+coords[1]*block_size[1]), (block_size[0]*number,block_size[1]))

        group.add(self)
        
class Level():
    def __init__(self,level,levelName,imageSet,offset, block_size):
        self.level = level # [[]]
        self.levelName = levelName
        self.imageSet = imageSet #0: фон 1: стена 2: пол
        self.levelBlocks = pygame.sprite.Group()
        self.walls = pygame.sprite.Group()

        x,y = 0,0
        for row in level:
            for element in row:
                img = self.imageSet[element]
                block = Block(img,(x,y),self.levelBlocks, offset, block_size, 1)
        
                if element == 1:
                    self.walls.add(block)
                x += 1
            x,y = 0,y+1

