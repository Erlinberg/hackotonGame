import pygame, os

class ImageLoader():
    def __init__(self):
        self.CreateDict()
        self.imageStorage = self.CreateDict()

    def CreateDict(self):
        result = {}

        for path, dirs, files in os.walk("Graphics"):
            if not path == "Graphics":
                key = path[9:]
                result[key] = []
                for f in files:
                    image = pygame.image.load("Graphics/{0}/{1}".format(key,f)).convert()
                    image.set_colorkey((0,255,0)) 
                    result[key].append(image)

        return result