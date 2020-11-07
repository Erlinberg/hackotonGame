import pygame
from Animator import Animation

class Block(pygame.sprite.Sprite):
    def __init__(self,image,coords, group, offset, block_size):
        super(Block, self).__init__()

        self.image = image
        self.rect = pygame.Rect((offset[0]+coords[0]*block_size[0], offset[1]+coords[1]*block_size[1]), (block_size[0],block_size[1]))

        group.add(self)

class Decoration(pygame.sprite.Sprite):
    def __init__(self,images,coords, group, offset, block_size):
        super(Decoration, self).__init__()

        self.images = images
        self.image = self.images[0]
        self.animationController = Animation(len(self.images),self)

        self.rect = pygame.Rect((offset[0]+coords[0]*block_size[0], offset[1]+coords[1]*block_size[1]), (block_size[0],block_size[1]))

        group.add(self)

        
    def update(self):
        if self.animationController.animCount > 0:
            self.animationController.animateRepeat(self.images, 1.4)
        
class Level():
    def __init__(self,levelName,imageSetLevel,imageSetDecoration,offset,block_size):
        self.level = self.getData("level.txt") # [[]]
        self.decorations = self.getData("deco.txt") # [[]]
        self.levelName = levelName
        self.imageSetLevel = imageSetLevel #0: фон 1: стена 2: пол

        self.imageSetDecoration = [imageSetDecoration[0:1],imageSetDecoration[1:4],[imageSetDecoration[4]],[imageSetDecoration[5]],[imageSetDecoration[6]],[imageSetDecoration[7]]] #0: фон 1: стена 2: пол
        
        self.levelBlocks = pygame.sprite.Group()
        self.walls = pygame.sprite.Group()

        self.decorationsGroup = pygame.sprite.Group()


        self.buildLevel(offset, block_size)
        self.buildDecoration(offset, block_size)

        

    
    def getData(self,name):
        data = []
        with open(name,mode="r") as file:
            data = [[int(element) for element in list(line.rstrip('\n'))] for line in file]
        return data


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

