import pygame

class Renderer():
    def __init__(self,WIDTH,HEIGHT):
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.screen = pygame.display.set_mode([WIDTH, HEIGHT], 0, 32)
        self.display = pygame.Surface((360,203))

        self.cameraOffset = [0,0]
        self.cameraSmoothness = 20

    def fillBackground(self):
            self.display.fill((0,0,0))

    def blitGroup(self, sprite_group):
        for sprite in sprite_group:
            self.display.blit(sprite.image, (sprite.rect.x-int(self.cameraOffset[0]),sprite.rect.y-int(self.cameraOffset[1])))

    def blitSprite(self,sprite):
        self.display.blit(sprite.image, (sprite.rect.x-int(self.cameraOffset[0]),sprite.rect.y-int(self.cameraOffset[1])))
    
    def blitUI(self,ui):
        self.screen.blit(ui.image, ui.rect)
    
    def drawLine(self,startPos,endPos,color,width):
        return pygame.draw.line(self.screen, color, startPos, endPos, width)

    def cameraUpdate(self,playerRect):
        self.cameraOffset[0] += (playerRect.x-self.cameraOffset[0]-self.WIDTH//4+playerRect.width//2)/self.cameraSmoothness
        self.cameraOffset[1] += (playerRect.y-self.cameraOffset[1]-self.HEIGHT//4+playerRect.height//2)/self.cameraSmoothness

    def update(self, isDark):
        if isDark:
            self.display.fill((75, 75, 100,0), special_flags=pygame.BLEND_RGBA_SUB)

        self.screen.blit(pygame.transform.scale(self.display,(self.WIDTH,self.HEIGHT)),(0,0))