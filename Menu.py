import pygame

class Button(pygame.sprite.Sprite):
    def __init__(self, image, centerPos, onclick, yOffset):
        self.image = image
        self.rect = self.image.get_rect()

        self.rect.center = centerPos
        self.rect.y -= yOffset

        self.onclick = onclick

    def update(self,mouseContoller):
        if mouseContoller.isLMBPressed and self.rect.collidepoint(mouseContoller.mousePos):
            self.onclick()


class Menu():
    def __init__(self,images, game):
        self.image = images[0]
        self.rect = self.image.get_rect()

        self.playButton = Button(images[1],self.rect.center,self.playButtonOnClick,100)
        self.quitButton = Button(images[2],self.rect.center,self.quitButtonOnClick,-50)

        self.game = game

    def playButtonOnClick(self):
        self.game.snowLevelInit()
        self.game.currentProgram = 'snow'

    def quitButtonOnClick(self):
        pygame.display.quit()
        pygame.quit()

    def update(self, mouseContoller, renderer):
        self.playButton.update(mouseContoller)
        self.quitButton.update(mouseContoller)

        renderer.blitUI(self)
        renderer.blitUI(self.playButton)
        renderer.blitUI(self.quitButton)