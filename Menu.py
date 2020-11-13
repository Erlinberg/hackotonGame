import pygame

class Button(pygame.sprite.Sprite):
    def __init__(self, image, pos, onclick):
        self.image = image
        self.rect = pygame.Rect(pos,self.image.get_size())

        self.onclick = onclick

    def update(self,mouseContoller):
        if mouseContoller.isLMBPressed and self.rect.collidepoint(mouseContoller.mousePos):
            self.onclick()


class Menu():
    def __init__(self,images, game):
        self.image = images[0]
        self.rect = self.image.get_rect()

        self.playButton = Button(images[2],(464,188),self.playButtonOnClick)
        self.quitButton = Button(images[1],(52,200),self.quitButtonOnClick,)

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